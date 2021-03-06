import streamlit as st
from misc import *


st.set_page_config(page_title = 'Evaluating Designs')


criteria_options = ['Average Absolute Correlation', 'Centered L2 Discrepancy',
                    'coverage','L2 Discrepancy', 'L2 Star Discrepancy', 'maximin',
                    'Maximum Absolute Correlation','Maximum Projection Criterion', 
                    'mixture L2 Discrepancy','meshratio','modified L2 Discrepancy',
                    'phi_p', 'symmetric L2 Discrepancy', 'wrap-around L2 Discrepancy']

uploaded_file = st.sidebar.file_uploader("Choose a file")

if uploaded_file is not None:
  
  evaldesign = st.form(key = 'evaldesign')
  criteria_type = evaldesign.selectbox('Choose Criteria to Evaluate Design:',
                                        options = criteria_options)
  submit_button = evaldesign.form_submit_button(label='Evaluate Design')
  
  if submit_button:
    design = pd.read_csv(uploaded_file).to_numpy()
    st.write(design)
    print_criteria(design,criteria_type,p=15,q=1)
  
                                            
                                          