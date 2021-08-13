import pyLHD
import streamlit as st
from misc import *

st.set_page_config(layout="wide")

st.sidebar.title('pyLHD')
st.sidebar.text('Latin hypercube design for Python')
design_type = st.sidebar.selectbox('Choose Design Type:',
                                   options = ('Random Latin Hypercube Design',
                                              'Good Lattice Point Design',
                                              'Orthogonal LHD (Butler 2001)',
                                              'Orthogonal LHD (Cioppa/Lucas 2007)',
                                              'Orthogonal LHD (Lin et al. 2009)',
                                              'Orthogonal LHD (Sun et al. 2010)',
                                              'Orthogonal LHD (Ye 1998)'))

gendesign = st.form(key = 'gendesign')

if design_type == 'Random Latin Hypercube Design':
  N = gendesign.number_input('Select number of rows',value=2,min_value=2)
  k = gendesign.number_input('Select number of columns',value=2,min_value=2)
  wt = gendesign.checkbox('Apply Williams Transformation')
  
  if wt:
    baseline_wt = gendesign.number_input('Select baseline for Williams Transformation',value=1,
                                         min_value=0)
    generated_design = pyLHD.williams_transform(pyLHD.rLHD(N,k),baseline=baseline_wt)
  else:
    generated_design = pyLHD.rLHD(N,k)
    
elif  design_type == 'Good Lattice Point Design':
  N = gendesign.number_input('Select number of rows',value=4,min_value=2)
  k = gendesign.number_input('Select number of columns',value=2,min_value=2)
  
  wt = gendesign.checkbox('Apply Williams Transformation')
  if wt:
    baseline_wt = gendesign.number_input('Select baseline for Williams Transformation',value=1,
                                        min_value=0)
    generated_design = pyLHD.williams_transform(pyLHD.GLPdesign(N,k),baseline=baseline_wt)
  else:
    generated_design = pyLHD.GLPdesign(N,k)

elif  design_type == 'Orthogonal LHD (Butler 2001)':
  N = gendesign.number_input('An odd prime number that is greater than or equal to 3 (N)',value=5,min_value=3,step=2)
  k = gendesign.number_input('A positive integer that is smaller than or equal to (N-1)',value=2,min_value=2)
  
  wt = gendesign.checkbox('Apply Williams Transformation')
  if wt:
    baseline_wt = gendesign.number_input('Select baseline for Williams Transformation',value=1,
                                        min_value=0)
    generated_design = pyLHD.williams_transform(pyLHD.OLHD_Butler01(N,k),baseline=baseline_wt)
  else:
    generated_design = pyLHD.OLHD_Butler01(N,k)

elif  design_type == 'Orthogonal LHD (Cioppa/Lucas 2007)':
  m = gendesign.number_input('Select a positive integer',value=2,min_value=2)

  wt = gendesign.checkbox('Apply Williams Transformation')
  if wt:
    baseline_wt = gendesign.number_input('Select baseline for Williams Transformation',value=1,
                                        min_value=0)
    generated_design = pyLHD.williams_transform(pyLHD.OLHD_Cioppa07(m=m),baseline=baseline_wt)
  else:
    generated_design = pyLHD.OLHD_Cioppa07(m=m)

elif  design_type == 'Orthogonal LHD (Sun et al. 2010)':
  C = gendesign.number_input('Select a positive integer (C)',value=5,min_value=1)
  r = gendesign.number_input('Select a positive integer (r)',value=2,min_value=1)
  type = gendesign.selectbox('Choose type:', ('even','odd') )
  
  wt = gendesign.checkbox('Apply Williams Transformation')
  if wt:
    baseline_wt = gendesign.number_input('Select baseline for Williams Transformation',value=1,
                                        min_value=0)
    generated_design = pyLHD.williams_transform(pyLHD.OLHD_Sun10(C=C,r=r,type=type),baseline=baseline_wt)
  else:
    generated_design = pyLHD.OLHD_Sun10(C=C,r=r,type=type)

elif  design_type == 'Orthogonal LHD (Ye 1998)':
  m = gendesign.number_input('Select a positive integer',value=2,min_value=2)

  wt = gendesign.checkbox('Apply Williams Transformation')
  if wt:
    baseline_wt = gendesign.number_input('Select baseline for Williams Transformation',value=1,
                                        min_value=0)
    generated_design = pyLHD.williams_transform(pyLHD.OLHD_Ye98(m=m),baseline=baseline_wt)
  else:
    generated_design = pyLHD.OLHD_Ye98(m=m)

elif design_type == 'Orthogonal LHD (Lin et al. 2009)':
  OLHD = gendesign.file_uploader('Upload an orthogonal Latin hypercube design (OLHD)')
  OA = gendesign.file_uploader('Upload an orthogonal array (OA)')
  
  if OLHD is not None and OA is not None:
    wt = gendesign.checkbox('Apply Williams Transformation')
    if wt:
      baseline_wt = gendesign.number_input('Select baseline for Williams Transformation',value=1,
                                          min_value=0)
      generated_design = pyLHD.williams_transform(pyLHD.OLHD_Lin09(OLHD,OA),baseline=baseline_wt)
    else:
      generated_design = pyLHD.OLHD_Lin09(OLHD,OA)
    
submit_button = gendesign.form_submit_button(label='Generate Design')

if submit_button:
  col1,col2 = st.columns(2)
  with col1:
    st.dataframe(pandas_design(generated_design))
  with col2:
    criteria_table(generated_design)
  design_txt_download(pandas_design(generated_design))
  design_csv_download(pandas_design(generated_design))