# 📦 Cálculo de Frete

## 📌 Problema
Empresas de logística precisam estimar o custo do frete com base em peso, preço e localização.

## 💡 Solução
Modelo de Machine Learning (Decision Tree) treinado com dados reais de e-commerce (Olist) e dashboard interativo com Streamlit.

🔗 **Acesse:** [calculo-frete.streamlit.app](https://calculo-frete-xqgnh9kclauananmzfflae.streamlit.app)

## 🎯 Resultados
- **Modelo:** Decision Tree com R² de 0.XX
- **Erro médio:** R$ XX,XX
- **Variáveis:** peso, preço, mesmo estado, estado do cliente

## 🛠️ Tecnologias
Python • Pandas • Scikit-learn • Streamlit

## 📂 Estrutura
calculo-frete/
├── data/
│ ├── olist_order_items_dataset.csv
│ ├── olist_orders_dataset.csv
│ └── olist_customers_dataset.csv
├── src/
│ └── dashboard.py
├── .streamlit/
│ └── config.toml
├── requirements.txt
└── README.md


## 🚀 Como Executar
```bash
pip install -r requirements.txt
streamlit run src/dashboard.py
