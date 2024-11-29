import streamlit as st
from streamlit_extras.grid import grid 
import db
import os
from pydub import AudioSegment
import io
import subprocess
import Prediction



def get_insights(dataset_file_name,audio_data):
    Prediction_grid = grid([1], vertical_align="centre")
    with Prediction_grid.container():
        Pred=Prediction.prediction(audio_data)
        res=int(Pred[0])
        if res==0:
            st.text_area("Prediction Result is:","Normal subject")
        else:
            st.text_area("Prediction Result is:","Murmur subject")
        st.text_area("Prediction time taken in millisecond",Pred[1])
                

def Prediction_gui():
    dataset_df = db.get_datasets_1()
    dataset_file_name = None
    audio_data=None
    if "uploaded_file" in st.session_state:
        uploaded_file=st.session_state['uploaded_file']
        audio_data = uploaded_file.read() 
    dataset_file_name = st.selectbox('Select a dataset',dataset_df['file_name'].tolist(), index=None, placeholder="Select a dataset...")
    
       
    model_name=st.selectbox('Select a model',('SVM','Xgboost','CNN'),index=None,placeholder="Select a model")
    pred_button=st.button("Perform Prediction on audio file",use_container_width=True)
    if model_name == 'SVM' and pred_button is not None:
        get_insights(dataset_file_name,audio_data)
        
        
        