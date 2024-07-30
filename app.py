import streamlit as st
from utils import GenotypeTransformer

import numpy as np
import pandas as pd
import joblib

load_svm = joblib.load('svm_pipe.joblib')
st.title('Predict Metabolisation Status :dna:')


star2 = st.selectbox("Enter CYP2C19*2 info", ['AG', 'GG', 'AA'])
star3 = st.selectbox("Enter CYP2C19*3 info", ['AG', 'GG'])
star17 = st.selectbox("Enter CYP2C19*17 info", ['TC','CC','TT'])
finalcode = st.selectbox("Enter patient heart condition", ['UA','STEMI','NSTEMI','Control'])
genotype_transformer = GenotypeTransformer("CYP2C19 Allele *2", "CYP2C19 Allele *3", "CYP2C19 Allele *17")


#Predict button
if st.button('Predict'):
    # Prepare the input data in the same format as the training data
    input_data = pd.DataFrame([[star2, star3, star17, finalcode]],
                              columns=['CYP2C19 Allele *2', 'CYP2C19 Allele *3', 'CYP2C19 Allele *17', 'FINAL CODE'])
    genotype = genotype_transformer.get_genotype(input_data.iloc[0])

    prediction = load_svm.predict(input_data)
    predicted_status = prediction[0]

    st.markdown(
        f"<h4 style='text-align: center;'>The predicted metabolisation status is: {predicted_status}</h4>", unsafe_allow_html=True)
    st.markdown(f"<h6 style='text-align: center;'>Genotype: {genotype}</h6>", unsafe_allow_html=True)



st.markdown(
    """
    <div style="position: fixed; bottom: 10px; right: 10px; opacity: 0.5;">
        <p style="font-size: 12px; font-style: italic;">
            Created by Ananya Gupta
        </p>
    </div>
    """, unsafe_allow_html=True
)


st.markdown(
    """
    <div style="position: fixed; bottom: 10px; left: 10px; opacity: 0.5;">
        <p style="font-size: 12px;">
            For more information, see:<br>
            Bhat, K. G., Pillai, R. K. J., Lodhi, H., Guleria, V. S., Abbot, A. K., Gupta, L., ... & Sharma, V. (2024).<br>
            Pharmacogenomic evaluation of CYP2C19 alleles linking low clopidogrel response and the risk<br> of acute coronary syndrome in Indians.
            The Journal of Gene Medicine, 26(1), e3634.
        </p>
    </div>
    """, unsafe_allow_html=True
)


