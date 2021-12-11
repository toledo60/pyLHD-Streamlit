import base64
import streamlit as st
import pandas as pd
import pyLHD

def download_link(object_to_download, download_filename, download_link_text):
        """
        Generates a link to download the given object_to_download.

        object_to_download (str, pd.DataFrame):  The object to be downloaded.
        download_filename (str): filename and extension of file. e.g. mydata.csv, some_txt_output.txt
        download_link_text (str): Text to display for download link.

        Examples:
        download_link(YOUR_DF, 'YOUR_DF.csv', 'Click here to download data!')
        download_link(YOUR_STRING, 'YOUR_STRING.txt', 'Click here to download your text!')

        """
        if isinstance(object_to_download, pd.DataFrame):
            object_to_download = object_to_download.to_csv(index=False)

        # some strings <-> bytes conversions necessary here
        b64 = base64.b64encode(object_to_download.encode()).decode()

        return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'

def design_txt_download(design):
  design_txt = design.to_csv(header=None, index=None, sep='\t', mode='a')
  design_txt_download = download_link(design_txt, 'design.txt','Download design as txt file')
  st.markdown(design_txt_download, unsafe_allow_html=True)
  
def design_csv_download(design):
  design_csv = design.to_csv(index=None)
  design_csv_download = download_link(design_csv, 'design.csv','Download design as csv file')
  st.markdown(design_csv_download, unsafe_allow_html=True)

def pandas_design(design):
  pd_design = pd.DataFrame(design,
                           columns=('col%d' % i for i in range(1,design.shape[1]+1)))
  pd_design.index = pd_design.index+1
  return pd_design


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
  return st.markdown(f'<p style="color:#F64167;">The {criteria} of this design: {result} </p>',
                     unsafe_allow_html=True)
  
  

  
