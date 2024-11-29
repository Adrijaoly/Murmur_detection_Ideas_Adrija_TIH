import streamlit as st
from streamlit_extras.grid import grid 
import db
import Analysis
import io
import os



dataset_file_name = None 


def get_insights(dataset_file_name,file_path):
    Analysis_grid = grid([1], vertical_align="centre")
    with Analysis_grid.container():
        audio_path=file_path
        plot=Analysis.show_PCG(audio_path)
        plot_1=Analysis.show_spectogram(audio_path)
        st.image(plot)
        st.image(plot_1)
        
        
        


def Analysis_gui():
    dataset_df = db.get_datasets_1()
    file_path=None
    if "audio_file_path" in st.session_state:
        file_path = st.session_state.audio_file_path
    dataset_file_name = None
    dataset_file_name = st.selectbox(
        'Select a dataset',dataset_df['file_name'].tolist(), index=None, placeholder="Select a dataset...")
    if dataset_file_name is not None:
        get_insights(dataset_file_name,file_path)