import pyLHD
import streamlit as st
from misc import *


st.set_page_config(page_title = 'Generating Designs')

design_type = st.sidebar.selectbox('Choose Design Type:',
                                  options = ('Random Latin Hypercube Design',
                                              'Lioness Algorithm for LHD',
                                              'Good Lattice Point Design',
                                              'Orthogonal LHD (Butler 2001)',
                                              'Orthogonal LHD (Cioppa/Lucas 2007)',
                                              'Orthogonal LHD (Lin et al. 2009)',
                                              'Orthogonal LHD (Sun et al. 2010)',
                                              'Orthogonal LHD (Ye 1998)'))

gendesign = st.form(key = 'gendesign')

if design_type == 'Random Latin Hypercube Design':
  gendesign.markdown('<p style="color:#F64167;">Generate a random (N by k) Latin hypercube design</p>',
                    unsafe_allow_html=True)
  N = gendesign.number_input('Select number of rows: (N)',value=2,min_value=2)
  k = gendesign.number_input('Select number of columns: (k)',value=2,min_value=2)
    
  wt = gendesign.checkbox('Apply Williams Transformation')
  
  if wt:
    baseline_wt = gendesign.number_input('Select baseline for Williams Transformation',value=1,
                                        min_value=0)
    generated_design = pyLHD.williams_transform(pyLHD.rLHD(N,k),baseline=baseline_wt)
  else:
    generated_design = pyLHD.rLHD(N,k)
    
elif design_type == 'Lioness Algorithm for LHD':
  gendesign.markdown('<p style="color:#F64167;">Apply Lioness Algorithm to a random (N by k) Latin hypercube design</p>',
                    unsafe_allow_html=True)
  N = gendesign.number_input('Select number of rows: (N)',value=2,min_value=2)
  k = gendesign.number_input('Select number of columns: (k)',value=2,min_value=2)
  m = gendesign.number_input('Select starting lionesses agents: (m)',value=10,min_value =10,max_value=100)
  it = gendesign.number_input('Select number of iterations to compute',value=10,min_value=10,max_value=500)
  LA_criteria = gendesign.selectbox('Choose optimality criteria',
                                options= ('phi_p','Average Absolute Correlation',
                                          'Maximum Absolute Correlation',
                                          'MaxProCriterion'))
  gendesign.markdown('<p style="color:#F64167;">Options below only apply to phi_p criterion</p>',
                    unsafe_allow_html=True)
  p = gendesign.number_input('p: (default is 15)',value=15,min_value=1,max_value=100)
  q = gendesign.selectbox('q: Distance Type',
                          options=('Manhattan (q=1)',
                                  'Euclidean (q=2)'))
  if LA_criteria == 'Average Absolute Correlation':
    LA_criteria = 'AvgAbsCor'
  if LA_criteria == 'Maximum Absolute Correlation':
    LA_criteria = 'MaxAbsCor'
  
  if q == 'Manhattan (q=1)':
    q=1
  else:
    q=2
  
  generated_design = pyLHD.LA_LHD(n=N,k=k,m=m,criteria=LA_criteria,
                                  N=it,q=q,p=p,maxtime=10)
  
  criteria = LA_criteria
  if criteria == 'AvgAbsCor':
    criteria = 'Average Absolute Correlation'
  if criteria == 'MaxAbsCor':
    criteria = 'Maximum Absolute Correlation'
    
elif design_type == 'Good Lattice Point Design':
  gendesign.markdown('<p style="color:#F64167;">Generate a (N by k) good lattice point design</p>',
                    unsafe_allow_html=True)
  gendesign.markdown('Note: k must be less than N')
  N = gendesign.number_input('Select number of rows: (N)',value=4,min_value=2)
  k = gendesign.number_input('Select number of columns: (k)',value=2,min_value=2)
    
  wt = gendesign.checkbox('Apply Williams Transformation')
  
  if wt:
    baseline_wt = gendesign.number_input('Select baseline for Williams Transformation',value=1,
                                        min_value=0)
    generated_design = pyLHD.williams_transform(pyLHD.GLPdesign(N,k),baseline=baseline_wt)
  else:
    generated_design = pyLHD.GLPdesign(N,k)

elif design_type == 'Orthogonal LHD (Butler 2001)':
  gendesign.markdown('<p style="color:#F64167;">Generate an orthogonal LHD based on Butler 2001 construction</p>',
                    unsafe_allow_html=True)  
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
  gendesign.markdown('<p style="color:#F64167;"> Generate an orthogonal LHD based on Cioppa and Lucas 2007 construction</p>',
                    unsafe_allow_html=True)
  gendesign.markdown('Design will have the following run size: $n=2^m+1$ and the following factor size: $k=m+{m-1 \\choose 2}$')
  m = gendesign.number_input('Select a positive integer (m)',value=2,min_value=2)
      
  wt = gendesign.checkbox('Apply Williams Transformation')
  if wt:
    baseline_wt = gendesign.number_input('Select baseline for Williams Transformation',value=1,
                                        min_value=0)
    generated_design = pyLHD.williams_transform(pyLHD.OLHD_Cioppa07(m=m),baseline=baseline_wt)
  else:
    generated_design = pyLHD.OLHD_Cioppa07(m=m)

elif  design_type == 'Orthogonal LHD (Sun et al. 2010)':
  gendesign.markdown('<p style="color:#F64167;"> Generate an orthogonal LHD based on Sun et al. 2010 construction</p>',
                    unsafe_allow_html=True)
  gendesign.markdown('If type is odd, design will have run size $(r2^{C+1}+1)$. If type is even, run size will be $(r2^{C+1})$. Factor size is $2^C$')
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
  gendesign.markdown('<p style="color:#F64167;"> Generate an orthogonal LHD based on Ye 1998 construction</p>',
                    unsafe_allow_html=True)
  gendesign.markdown('Design will have the following run size: $n=2^m+1$ and the following factor size: $k=2m-2$')
  m = gendesign.number_input('Select a positive integer (m)',value=2,min_value=2)
      
  wt = gendesign.checkbox('Apply Williams Transformation')
  if wt:
    baseline_wt = gendesign.number_input('Select baseline for Williams Transformation',value=1,
                                        min_value=0)
    generated_design = pyLHD.williams_transform(pyLHD.OLHD_Ye98(m=m),baseline=baseline_wt)
  else:
    generated_design = pyLHD.OLHD_Ye98(m=m)

elif design_type == 'Orthogonal LHD (Lin et al. 2009)':
  gendesign.markdown('<p style="color:#F64167;"> Generate an orthogonal LHD based on Lin et al. 2009 construction</p>',
                    unsafe_allow_html=True)
  gendesign.markdown('OLHD: An orthogonal LHD with run size $n$ and factor size $p$')
  gendesign.markdown('OA: An orthogonal array, with $n^2$ rows, $2f$ columns, $n$ symbols, strength two and index unity is available, which can be denoted as $OA(n^2,2f,n,2)$ ')
  gendesign.markdown('After correct input of OLHD and OA, resulting design will have the following run size: $n^2$ and the following factor size: $2fp$')
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
  st.dataframe(pandas_design(generated_design).style.format("{:3}"))
  
  df = design_df(generated_design)
  st.download_button(
    label="Download Design as CSV",
    data=df,
    file_name= f'design_{generated_design.shape[0]}by{generated_design.shape[1]}.csv',
    mime='text/csv'
    )

