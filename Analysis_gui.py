import streamlit as st
from streamlit_extras.grid import grid 
import db
import Analysis
import io
import os



dataset_file_name = None 


def get_insights(dataset_file_name,audio_data):
    Analysis_grid = grid([1], vertical_align="centre")
    with Analysis_grid.container():
        plot=Analysis.show_PCG(audio_data)
        plot_1=Analysis.show_spectogram(audio_data)
        st.image(plot)
        st.image(plot_1)
        
        
        


def Analysis_gui():
    dataset_df = db.get_datasets_1()
    audio_data=None
    if "uploaded_file" in st.session_state:
        uploaded_file = st.session_state['uploaded_file']
        audio_data = uploaded_file.read()        
    dataset_file_name = None
    dataset_file_name = st.selectbox(
        'Select a dataset',dataset_df['file_name'].tolist(), index=None, placeholder="Select a dataset...")
    if dataset_file_name is not None:
        get_insights(dataset_file_name,audio_data)