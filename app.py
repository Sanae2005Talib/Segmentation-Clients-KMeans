import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Config dyal l-page (Dark Mode)
st.set_page_config(page_title="IA Dashboard", layout="wide")

# Design CSS  (Orange/Red)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    h1, h2, h3 { color: #ff4b2b !important; }
    [data-testid="stMetric"] {
        background-color: #1c2128;
        border-left: 5px solid #ff4b2b;
        padding: 20px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Load Data
try:
    df = pd.read_csv("segment.csv")
except:
    st.error("Fichier 'segment.csv' introuvable !")
    st.stop()

# 3. Sidebar
st.sidebar.title("🔥 Paramètres")
all_segments = sorted(df['Segment'].unique())
selected = st.sidebar.multiselect("🎯 Segments", all_segments, default=all_segments)

df_filtered = df[df['Segment'].isin(selected)]

# 4. Dashboard Header
st.title("📊 Customer Segmentation IA")
st.markdown("---")

# Metrics f l-foq
c1, c2, c3 = st.columns(3)
c1.metric("Clients", len(df_filtered))
c2.metric("Total (DH)", f"{df_filtered['TotalAmount'].sum():,.0f}")
c3.metric("Moyenne", f"{df_filtered['TotalAmount'].mean():,.2f}")

st.markdown("###")

# 5. Visualisation (Fikssina l-erreur dyal scatter)
col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("🔥 Map de Segmentation")
    
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('#0e1117')
    ax.set_facecolor('#1c2128')

    # Scatter plot n9i (T-akkdi mn l-tartib dyal had les arguments)
    scatter = ax.scatter(
        df_filtered['Quantity'], 
        df_filtered['TotalAmount'], 
        c=df_filtered['Segment'], 
        cmap='YlOrRd', 
        alpha=0.8,
        edgecolors='white'
    )

    ax.set_xlabel("Quantité", color='white')
    ax.set_ylabel("Montant", color='white')
    ax.tick_params(colors='white')
    
    st.pyplot(fig)

with col_right:
    st.subheader("📈 Stats Moyennes")
    stats = df_filtered.groupby('Segment')[['Quantity', 'TotalAmount']].mean()
    # Design du tableau avec couleurs
    st.dataframe(stats.style.background_gradient(cmap='OrRd'))

# 6. Data Explorer
with st.expander("📂 Raw Data Explorer"):
    st.dataframe(df_filtered, use_container_width=True)