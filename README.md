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

## 📊 Insights de Negócio

### Como o Frete é Calculado

O frete no Brasil é composto por **três partes principais**:

| Componente | Base de Cálculo | Finalidade |
| :--- | :--- | :--- |
| **Frete-Peso** | Peso (kg) × Distância | Cobrir custos de transporte (combustível, pneus, motorista) |
| **Frete-Valor** | % sobre o Valor da Mercadoria | Cobrir risco de perda, avaria ou roubo |
| **GRIS** | % sobre o Valor da Mercadoria | Cobrir custos de gerenciamento de risco (seguro, rastreamento, escolta) |

**Fórmula do Frete Total:**

Frete Total = (Peso × Tarifa/kg) + (Valor da Carga × % Frete-Valor) + (Valor da Carga × % GRIS)


### O que é o GRIS?

**GRIS** significa **Gerenciamento de Risco e Seguro**. É uma taxa percentual cobrada sobre o valor da mercadoria para cobrir os custos de:

- **Seguro RCF-DC:** Proteção contra roubo, furto e avarias.
- **Rastreamento:** Monitoramento em tempo real, câmeras, telemetria.
- **Escolta:** Segurança armada em rotas de risco.
- **Tecnologia:** Sistemas de rastreamento e taxas de habilitação.

**Valor de referência no mercado:** ~0,30% sobre o valor da carga (mínimo de R$ 3,00 por conhecimento).

### Frete Intraestadual vs. Interestadual

| Tipo | O que é | Impacto no Frete |
| :--- | :--- | :--- |
| **Intraestadual** | Cliente e vendedor no mesmo estado | Frete mais barato (distância menor, menos risco) |
| **Interestadual** | Cliente e vendedor em estados diferentes | Frete mais caro (distância maior, mais pedágio, mais risco) |

**Insight do modelo:** Fretes entre estados diferentes são, em média, **3x mais caros** que fretes dentro do mesmo estado.

### Principais Insights do Projeto

1.  **Peso é o fator mais importante:** O peso da carga é a variável que mais impacta o custo do frete.
2.  **Frete interestadual é mais caro:** A distância entre estados diferentes aumenta significativamente o valor.
3.  **Estados do Norte e Nordeste têm fretes mais caros:** Devido à distância e à logística complexa.
4.  **Oportunidade:** Negociar fretes para cargas pesadas ou para regiões específicas pode gerar economia significativa.

### Como Cada Empresa Define Sua Tabela

Cada transportadora cria sua própria **Tabela de Tarifas**, baseada em:

| Fator | O que influencia |
| :--- | :--- |
| **Custos operacionais** | Combustível, pneus, manutenção, salários |
| **Região de atuação** | Rotas mais perigosas = GRIS maior |
| **Tipo de carga** | Eletrônicos = Frete-Valor maior |
| **Volume de carga** | Mais volume = tarifas menores |
| **Histórico de sinistros** | Mais roubos = GRIS maior |

**Importante:** Todas as empresas devem respeitar o **Piso Mínimo ANTT**, que é o valor mínimo que pode ser cobrado por lei.

📬 Contato
Jeferson Gomes

LinkedIn

GitHub
