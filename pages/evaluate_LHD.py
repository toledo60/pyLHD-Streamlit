import pyLHD
import streamlit as st
from pages.misc import *

def app():  
  criteria_options = ['Average Absolute Correlation', 'Centered L2 Discrepancy',
                    'L2 Discrepancy', 'L2 Star Discrepancy', 'Maximum Absolute Correlation',
                    'Maximum Projection Criterion', 'mixture L2 Discrepancy', 'modified L2 Discrepancy',
                    'phi_p', 'symmetric L2 Discrepancy', 'wrap-around L2 Discrepancy']
  
  criteria_type = st.sidebar.selectbox('Choose Criteria to Evaluate Design:',
                                    options = criteria_options)
                                            
                                          