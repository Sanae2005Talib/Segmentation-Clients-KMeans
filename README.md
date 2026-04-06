#  Customer Segmentation Dashboard (K-Means)

##  Description du Projet
Ce projet consiste à développer une solution complète de segmentation client en utilisant l'Intelligence Artificielle (Algorithme K-Means) et une interface interactive avec **Streamlit**. 

L’objectif est d’analyser le comportement d'achat des clients afin d’aider à la prise de décision marketing basée sur des segments réels.

---

##  Contenu du Dépôt
- **`Analyse_Clustering.ipynb`** : Notebook (Google Colab) contenant le nettoyage des données et l'entraînement du modèle.
- **`app_streamlit.py`** : Code source de l'application interactive (Dashboard).
- **`dataset_cleaned.csv`** : Le jeu de données prétraité utilisé pour le clustering.
- **`Rapport_Projet_IA.pdf`** : Documentation technique détaillée (10 pages).
- **`Presentation_Soutenance.pptx`** : Support visuel pour la présentation orale.

---

##  Technologies Utilisées
- **Langage** : Python 3.14
- **Libraries** : Pandas, NumPy, Matplotlib, Scikit-learn
- **Interface** : Streamlit

---

##  Dataset
Le dataset utilisé provient de **Kaggle (Online Retail Dataset)**. Il contient des transactions e-commerce avec les variables suivantes :
- `CustomerID`, `Quantity`, `UnitPrice`, `InvoiceDate`, `Country`.

---

##  Modèle Machine Learning
- **Type** : Clustering (Apprentissage non-supervisé).
- **Algorithme** : K-Means.
- **Variables d'entrée** : Quantity & TotalAmount.

---

##  Résultats
Les clients ont été divisés en 3 segments clés :
1. **Segment VIP (Importants)** : Clients avec un volume d'achat très élevé.
2. **Segment Standard (Moyens)** : Clients réguliers avec un panier moyen.
3. **Segment Occasionnels (Faibles)** : Clients avec peu de transactions.

---

##  Lancer le Projet

### 1️ Installer les dépendances
```bash
pip install streamlit pandas matplotlib scikit-learn
