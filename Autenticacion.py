import pandas as pd
import streamlit as st

uri=st.secrets.db_credentials.URI

def contraseña(usuario):

    contraseña= pd.read_sql(f"select contraseña from usuarios where usuario = '{usuario}' AND estado='Activo'",uri)
    contraseña = contraseña.loc[0,'contraseña']
    return contraseña
