import streamlit as st
import pandas as pd
import numpy as np

# Titolo dell'app
st.title("🧮 Calcolatrice Semplice")
st.write("Esegui somme e sottrazioni in modo facile!")

# Sezione Somma
st.header("➕ Somma")
col1, col2 = st.columns(2)

with col1:
    num1_somma = st.number_input("Primo numero", value=0.0, key="somma1")
with col2:
    num2_somma = st.number_input("Secondo numero", value=0.0, key="somma2")

if st.button("Calcola Somma", type="primary"):
    risultato_somma = num1_somma + num2_somma
    st.success(f"✅ Risultato: {num1_somma} + {num2_somma} = **{risultato_somma}**")

st.divider()

# Sezione Sottrazione
st.header("➖ Sottrazione")
col3, col4 = st.columns(2)

with col3:
    num1_sottrazione = st.number_input("Primo numero", value=0.0, key="sott1")
with col4:
    num2_sottrazione = st.number_input("Secondo numero", value=0.0, key="sott2")

if st.button("Calcola Sottrazione", type="primary"):
    risultato_sottrazione = num1_sottrazione - num2_sottrazione
    st.success(f"✅ Risultato: {num1_sottrazione} - {num2_sottrazione} = **{risultato_sottrazione}**")


x = np.linspace(0, 1, 1000)
y = np.random.randn(1000)
df = pd.DataFrame([x, y], columns=["x", "y"])


st.line_chart(df)

# Footer
st.divider()
st.caption("💡 Inserisci i numeri e clicca sul pulsante per vedere il risultato!")