#importation des librairies
import streamlit as st
from pycaret.classification import load_model,predict_model
import pandas

#insérer un titre
st.title("Streamlit - Déploiement modèle ML")

#mise en cache du chargement du modle 
@st.cache_resource
def chargement_modele():
    return load_model("modele_trained")

#chargement effectif
modele=chargement_modele()

#organisation en 2 colonnes (1/4, 3/4)
col1,col2=st.columns([1,3])

#text_input: aligné sur la première colonne
SepalLengthCm=col1.text_input("Sepal length : ","5.2",max_chars=3)
SepalWidthCm=col1.text_input("Sepal width : ","2.4",max_chars=3)
PetalLengthCm=col1.text_input("Petal length : ","2.4",max_chars=3)
PetalWidthCm=col1.text_input("Pepal width : ","3.4",max_chars=3)


#focntion pour la gestion des erreur de saisie

def try_parse(str_value):
    try:
        val=float(str_value)
    except Exception:
        val=float('NaN')
    return val

# conversion en dictionnaire des données  récupérer via le formulaire de saisie
dic_data={"SepalLengthCm":try_parse(SepalLengthCm),
          "SepalWidthCm":try_parse(SepalWidthCm),
          "PetalLengthCm":try_parse(PetalLengthCm),
          "PetalWidthCm":try_parse(PetalWidthCm)}

# calcul de la classe d'appartenance

try:
    dic_data=predict_model(modele,data=pandas.DataFrame([dic_data]))
except Exception:
    dic_data="inconnu"

# bouton pour lancer les calculs
st.button("Prediction")   

#affichage de la classe prédit
st.write("Classe d'appartenance:",dic_data[['prediction_label','prediction_score']])
