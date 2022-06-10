import streamlit as st

# Title of the main page
st.set_page_config(page_title = 'pyLHD Streamlit Application')

st.title("pyLHD-Steamlit Application")
st.text("Latin Hypecubes for Python")
st.markdown('[Check out pyLHD on Github](https://github.com/toledo60/pyLHD)')

st.markdown("""
For this application 
- Generate design *(see below for construction methods)*. Then download generated design as CSV
- Using the downloaded design *(CSV)* you can evaluate the design to calucate its space-filling properties *(see below for calculated properties)*
            
With `pyLHD` you can generate the following designs *(Generate LHD tab)*:

- `rLHD`: Generate a random Latin hypercube design
- `GLPdesign`: Generate a good lattice point design
- `OLHD_Butler01`: Orthogonal Latin hypercube design. Based on the construction method of Butler (2001)
- `OLHD_Cioppa07`: Orthogonal Latin hypercube design. Based on the construction method of Cioppa and Lucas (2007)
- `OLHD_Lin09`: Orthogonal Latin hypercube design. Based on the construction method of Lin et al. (2009)
- `OLHD_Sun10`: Orthogonal Latin hypercube design. Based on the construction method of Sun et al. (2010)
- `OLHD_Ye98`: Orthogonal Latin hypercube design. Based on the construction method of Ye (1998)

Calculate design properties *(Evaluate LHD tab)* such as:

- `AvgAbsCor`: Calculate the average absolute correlation
- `dij`: Calculate the Inter-site Distance (rectangular/Euclidean) between the *ith* and *jth* row
- `coverage`: Calculate the coverage measure
- `discrepancy`: Calculate the discrepancy of a given sample
- `MaxAbsCor`: Calculate the maximum absolute correlation
- `MaxProCriterion`: Calculate the maximum projection criterion
- `mesh_ratio`: Calculate the meshratio criterion
- `minimax`: Calculate the minimax criterion
- `phi_p`: Calculate the phi_p criterion

Optimization algorithms to improve LHD's based on desired criteria:

- `LA_LHD`: Lioness Algorithm for Latin hypercube design
- `SA_LHD`: Simulated Annealing for Latin hypercube design            
            
            """)
