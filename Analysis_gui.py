import streamlit as st
from streamlit_extras.grid import grid 
import db
import Analysis
import io
import os
import soundfile as sf
import numpy as np
from io import BytesIO
from pydub import AudioSegment

dataset_file_name = None 


def get_insights(dataset_file_name,file_path):
    Analysis_grid = grid([1], vertical_align="centre")
    with Analysis_grid.container():
        #tab1,tab2=st.tabs(['PCG','MFCC'])  
        # wav_data = os.listdir(r"C:\Adrija_1\user_data")
        # base_path = r"C:\Adrija_1\user_data"
        audio_path=file_path
        plot=Analysis.show_PCG(audio_path)
        plot_1=Analysis.show_spectogram(audio_path)
        st.image(plot)
        st.image(plot_1)
        # for each_file in wav_data:
        #     full_path = os.path.join(base_path, each_file)
        #     plot=Analysis.show_PCG(full_path)
        #     plot_1=Analysis.show_spectogram(full_path)
        #     st.image(plot)
        #     st.image(plot_1)
        
        
        


def Analysis_gui():
    dataset_df = db.get_datasets_1()
    if "audio_file_path" in st.session_state:
        file_path = st.session_state.audio_file_path
    dataset_file_name = None
    dataset_file_name = st.selectbox(
        'Select a dataset',dataset_df['file_name'].tolist(), index=None, placeholder="Select a dataset...")
    if dataset_file_name is not None:
        get_insights(dataset_file_name,file_path)