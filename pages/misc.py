import streamlit as st
import pandas as pd
import pyLHD

def pandas_design(design):
  pd_design = pd.DataFrame(design,
                           columns=('col%d' % i for i in range(1,design.shape[1]+1)))
  pd_design.index = pd_design.index+1
  return pd_design

@st.cache
def design_df(design):
  df = pd.DataFrame(design)
  return df.to_csv(index=None).encode('utf-8')


def print_criteria(design,criteria,p=15,q=1):
  
  if criteria=='Average Absolute Correlation':
    result =  pyLHD.AvgAbsCor(design)
  elif criteria == 'Maximum Absolute Correlation':
    result = pyLHD.MaxAbsCor(design)
  elif criteria == 'Maximum Projection Criterion':
    result = pyLHD.MaxProCriterion(design)
  elif criteria == 'phi_p':
    result = pyLHD.phi_p(design,p=p,q=q)
  elif criteria == 'L2 Discrepancy':
    result = pyLHD.discrepancy(design,'L2')
  elif criteria == 'L2 Star Discrepancy':
    result = pyLHD.discrepancy(design,'L2_star')
  elif criteria == 'modified L2 Discrepancy':
    result = pyLHD.discrepancy(design,'modified_L2')
  elif criteria == 'mixture L2 Discrepancy':
    result = pyLHD.discrepancy(design,'mixture_L2')
  elif criteria == 'symmetric L2 Discrepancy':
    result = pyLHD.discrepancy(design,'symmetric_L2')
  elif criteria == 'wrap-around L2 Discrepancy':
    result = pyLHD.discrepancy(design,'wrap_around_L2')
  elif criteria == 'Centered L2 Discrepancy':
    result =  pyLHD.discrepancy(design)
  elif criteria == 'maximin':
    result = pyLHD.maximin(design)
  elif criteria == 'meshratio':
    result = pyLHD.mesh_ratio(design)
  elif criteria == 'coverage':
    result = pyLHD.coverage(design)
    
  st.markdown(f'<p style="color:#F64167;">The {criteria} of this design: {result} </p>',
              unsafe_allow_html=True)
    

# Define the multipage class to manage the multiple apps in our program 
class MultiPage: 
  """Framework for combining multiple streamlit applications."""

  def __init__(self) -> None:
    """Constructor class to generate a list which will store all our applications as an instance variable."""
    self.pages = []
  
  def add_page(self, title, func) -> None: 
    """Class Method to Add pages to the project
    Args:
        title ([str]): The title of page which we are adding to the list of apps 
        
        func: Python function to render this page in Streamlit
    """

    self.pages.append({
      
            "title": title, 
            "function": func
        })

  def run(self):
    # Drodown to select the page to run  
    page = st.sidebar.selectbox(
        'App Navigation', 
        self.pages, 
        format_func=lambda page: page['title']
    )

    # run the app function 
    page['function']()