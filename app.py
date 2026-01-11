import streamlit as st
import pickle
import numpy as np

# Chargement sécurisé
try:
    model = pickle.load(open('model_diabete.pkl', 'rb'))
    scaler = pickle.load(open('scaler.pkl', 'rb'))
except:
    st.error("Erreur : Fichiers manquants. Relancez les cellules de sauvegarde dans Colab.")

st.title("🩺 Diagnostic Diabète IA")

# On crée les entrées
bmi = st.number_input("IMC (BMI)", value=22.0)
age = st.number_input("Âge", value=25)
glucose = st.number_input("Glucose", value=90)
bp = st.number_input("Pression Artérielle", value=70)
ins = st.number_input("Insuline", value=15)

if st.button("Analyser"):
    # L'ORDRE DOIT ÊTRE IDENTIQUE À TON X_train : BMI, Age, Glucose, BloodPressure, Insulin
    features = np.array([[bmi, age, glucose, bp, ins]])
    
    # APPLICATION DU SCALER (INDISPENSABLE)
    features_scaled = scaler.transform(features)
    
    prediction = model.predict(features_scaled)
    probability = model.predict_proba(features_scaled)[0][1] * 100
    
    st.markdown("---")
    if prediction[0] == 1:
        st.error(f"### ⚠️ Risque Élevé ({probability:.1f}%)")
    else:
        st.success(f"### ✅ Risque Faible ({100 - probability:.1f}% de chance d'être sain)")
