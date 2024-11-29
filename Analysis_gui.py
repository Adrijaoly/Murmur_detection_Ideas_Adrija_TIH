import streamlit as st
from streamlit_extras.grid import grid 
import db
import Analysis
import io
import os



dataset_file_name = None 


def get_insights(dataset_file_name,dataset_df):
    Analysis_grid = grid([1], vertical_align="centre")
    with Analysis_grid.container():
        #tab1,tab2=st.tabs(['PCG','MFCC'])  
        wav_data = os.listdir("dataset_files/")
        base_path = "dataset_files/"
        for each_file in wav_data:
            full_path = os.path.join(base_path, each_file)
            plot=Analysis.show_PCG(full_path)
            plot_1=Analysis.show_spectogram(full_path)
            st.image(plot)
            st.image(plot_1)
        
        
        


def Analysis_gui():
    dataset_df = db.get_datasets_1()
    print(dataset_df)
    dataset_file_name = None
    dataset_file_name = st.selectbox(
        'Select a dataset',dataset_df['file_name'].tolist(), index=None, placeholder="Select a dataset...")
    if dataset_file_name is not None:
        get_insights(dataset_file_name,dataset_df)