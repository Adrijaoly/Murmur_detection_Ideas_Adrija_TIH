import streamlit as st
from streamlit_extras.grid import grid 
import db
import os
from pydub import AudioSegment
import io
import subprocess
import Prediction



def get_insights(dataset_file_name,dataset_df):
    Prediction_grid = grid([1], vertical_align="centre")
    with Prediction_grid.container():
        #tab1,tab2=st.tabs(['PCG','MFCC'])  
        wav_data = os.listdir("dataset_files/")
        base_path = "dataset_files/"
        for each_file in wav_data:
            full_path = os.path.join(base_path, each_file)
            Pred=Prediction.prediction(full_path)
            res=int(Pred[0])
            if res==0:
               st.text_area("Prediction Result is:","Normal subject")
            else:
                st.text_area("Prediction Result is:","Murmur subject")
            st.text_area("Prediction time taken in millisecond",Pred[1])
                

def Prediction_gui():
    dataset_df = db.get_datasets_1()
    dataset_file_name = None
    dataset_file_name = st.selectbox('Select a dataset',dataset_df['file_name'].tolist(), index=None, placeholder="Select a dataset...")
    # if dataset_file_name is not None:
    #     file_path = os.path.join("dataset_files/",dataset_file_name)
    #     print(file_path)
    #     output_file_path=os.path.join(r"C:\Adrija_1\user_data", "converted_" + os.path.splitext(dataset_file_name)[0] + ".wav")
    #     subprocess.run([
    #         "ffmpeg",
    #         "-i", file_path,        
    #         "-c:a", "pcm_s16le",     
    #         "-ar", "44100",          
    #         "-ac", "2",              
    #         output_file_path], check=True)
    # st.audio(output_file_path, format="audio/mpeg")
        
    model_name=st.selectbox('Select a model',('SVM','Xgboost','CNN'),index=None,placeholder="Select a model")
    pred_button=st.button("Perform Prediction on audio file",use_container_width=True)
    if model_name == 'SVM' and pred_button is not None:
        get_insights(dataset_file_name,dataset_df)
        
        
        