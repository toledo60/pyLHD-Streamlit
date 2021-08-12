import pyLHD
import streamlit as st
import numpy as np
import pandas as pd


design_type = st.sidebar.selectbox('Choose Design Type:',
                                   options = ('Random Latin Hypercube Design',
                                              'Good Lattice Point Design',
                                              'Orthogonal LHD (Butler 2001)',
                                              'Orthogonal LHD (Cioppa/Lucas 2007)',
                                              'Orthogonal LHD (Lin et al. 2009)',
                                              'Orthogonal LHD (Sun et al. 2010)',
                                              'Orthogonal LHD (Ye 1998)'))

