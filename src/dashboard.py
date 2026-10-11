import streamlit as st
import pandas as pd
import numpy as np
import os
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import LabelEncoder

st.set_page_config(page_title="Calculadora de Frete", page_icon="📦", layout="wide")

st.title("📦 Calculadora de Frete")
st.markdown("""
Esta aplicação estima o custo do frete com base em características da entrega.
Desenvolvido por [Jeferson Gomes](https://github.com/jeferson-data).
""")

@st.cache_resource
def treinar_modelo():
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Carregar apenas 3 CSVs
    items = pd.read_csv(os.path.join(base_path, 'data/olist_order_items_dataset.csv'))
    orders = pd.read_csv(os.path.join(base_path, 'data/olist_orders_dataset.csv'))
    customers = pd.read_csv(os.path.join(base_path, 'data/olist_customers_dataset.csv'))
    
    # Juntar
    df = items.merge(orders[['order_id', 'customer_id']], on='order_id', how='left')
    df = df.merge(customers[['customer_id', 'customer_state']], on='customer_id', how='left')
    
    # Limpeza
    df = df.dropna(subset=['freight_value', 'customer_state'])
    df = df[df['freight_value'] < df['freight_value'].quantile(0.99)]
    
    # Features
    df['peso_kg'] = 2.0  # Valor fixo (média do Olist)
    df['mesmo_estado'] = 1  # Assume que cliente e vendedor estão no mesmo estado
    
    # Encoder
    le_customer = LabelEncoder()
    df['customer_state_encoded'] = le_customer.fit_transform(df['customer_state'])
    
    # Modelo leve
    features = ['peso_kg', 'price', 'mesmo_estado', 'customer_state_encoded']
    X = df[features]
    y = df['freight_value']
    
    modelo = DecisionTreeRegressor(max_depth=10, min_samples_leaf=50, random_state=42)
    modelo.fit(X, y)
    
    return modelo, le_customer

try:
    with st.spinner('Carregando modelo...'):
        modelo, le_customer = treinar_modelo()
    st.sidebar.success("✅ Modelo carregado!")
except Exception as e:
    st.error(f"❌ Erro: {e}")
    st.stop()

st.sidebar.header("📋 Dados da Entrega")

peso_kg = st.sidebar.number_input("Peso (kg)", min_value=0.1, max_value=100.0, value=5.0, step=0.1)
preco = st.sidebar.number_input("Preço (R$)", min_value=1.0, max_value=10000.0, value=100.0, step=10.0)
mesmo_estado_opcao = st.sidebar.selectbox("Mesmo estado?", ["Sim", "Não"])
mesmo_estado = 1 if mesmo_estado_opcao == "Sim" else 0

estados = ['SP', 'RJ', 'MG', 'RS', 'PR', 'SC', 'BA', 'PE', 'CE', 'DF']
customer_state = st.sidebar.selectbox("Estado do cliente", estados)

if st.sidebar.button("Calcular Frete", type="primary"):
    try:
        customer_state_encoded = le_customer.transform([customer_state])[0]
        
        dados = pd.DataFrame({
            'peso_kg': [peso_kg],
            'price': [preco],
            'mesmo_estado': [mesmo_estado],
            'customer_state_encoded': [customer_state_encoded]
        })
        
        previsao = modelo.predict(dados)[0]
        
        st.success(f"### 💰 Custo estimado do frete: R$ {previsao:.2f}")
        
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        col1.metric("Peso", f"{peso_kg:.2f} kg")
        col2.metric("Preço", f"R$ {preco:.2f}")
        col3.metric("Mesmo Estado", "Sim" if mesmo_estado == 1 else "Não")
    except Exception as e:
        st.error(f"Erro: {e}")

st.markdown("---")
st.markdown("Desenvolvido por [Jeferson Gomes](https://github.com/jeferson-data)")