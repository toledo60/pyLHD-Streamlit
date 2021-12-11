import pyLHD
import streamlit as st
from misc import *

st.set_page_config(layout="wide")

st.sidebar.title('pyLHD')
st.sidebar.text('Latin hypercube design for Python')
design_type = st.sidebar.selectbox('Choose Design Type:',
                                   options = ('Random Latin Hypercube Design',
                                              'Lioness Algorithm for LHD',
                                              'Good Lattice Point Design',
                                              'Orthogonal LHD (Butler 2001)',
                                              'Orthogonal LHD (Cioppa/Lucas 2007)',
                                              'Orthogonal LHD (Lin et al. 2009)',
                                              'Orthogonal LHD (Sun et al. 2010)',
                                              'Orthogonal LHD (Ye 1998)'))

st.sidebar.markdown('[Check out pyLHD on Github](https://github.com/toledo60/pyLHD)')
gendesign = st.form(key = 'gendesign')

criteria_options = ['Average Absolute Correlation', 'Centered L2 Discrepancy',
                    'L2 Discrepancy', 'L2 Star Discrepancy', 'Maximum Absolute Correlation',
                    'Maximum Projection Criterion', 'mixture L2 Discrepancy', 'modified L2 Discrepancy',
                    'phi_p', 'symmetric L2 Discrepancy', 'wrap-around L2 Discrepancy']

if design_type == 'Random Latin Hypercube Design':
  gendesign.markdown('<p style="color:#F64167;">Generate a random (N by k) Latin hypercube design</p>',
                     unsafe_allow_html=True)
  N = gendesign.number_input('Select number of rows: (N)',value=2,min_value=2)
  k = gendesign.number_input('Select number of columns: (k)',value=2,min_value=2)
  criteria = gendesign.selectbox('Choose Criteria:',
                                  options= criteria_options )
    
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
  criteria = gendesign.selectbox('Choose optimality criteria',
                                 options= ('phi_p','Average Absolute Correlation',
                                           'Maximum Absolute Correlation',
                                           'MaxProCriterion'))
  gendesign.markdown('<p style="color:#F64167;">Options below only apply to phi_p criterion</p>',
                     unsafe_allow_html=True)
  p = gendesign.number_input('p: (default is 15)',value=15,min_value=1,max_value=100)
  q = gendesign.selectbox('q: Distance Type',
                          options=('Manhattan (q=1)',
                                   'Euclidean (q=2)'))
  
  if q == 'Manhattan (q=1)':
    q=1
  else:
    q=2
  
  generated_design = pyLHD.LA_LHD(n=N,k=k,m=m,criteria=criteria,
                                  N=it,q=q,p=p,maxtime=10)
  
elif design_type == 'Good Lattice Point Design':
  gendesign.markdown('<p style="color:#F64167;">Generate a (N by k) good lattice point design</p>',
                     unsafe_allow_html=True)
  gendesign.markdown('Note: k must be less than N')
  N = gendesign.number_input('Select number of rows: (N)',value=4,min_value=2)
  k = gendesign.number_input('Select number of columns: (k)',value=2,min_value=2)
  criteria = gendesign.selectbox('Choose Criteria:',
                                  options= criteria_options )  
    
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
  criteria = gendesign.selectbox('Choose Criteria:',
                                  options= criteria_options ) 
       
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
  criteria = gendesign.selectbox('Choose Criteria:',
                                 options= criteria_options )
      
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
  criteria = gendesign.selectbox('Choose Criteria:',
                                  options= criteria_options )
      
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
  criteria = gendesign.selectbox('Choose Criteria:',
                                  options= criteria_options )
      
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
  criteria = gendesign.selectbox('Choose Criteria:',
                                  options= criteria_options )
        
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
  print_criteria(generated_design,criteria,p=15,q=1)
  st.dataframe(pandas_design(generated_design).style.format("{:3}"))
  
  design_txt_download(pandas_design(generated_design))
  design_csv_download(pandas_design(generated_design))