# ----- Librerías ---- #

import streamlit as st
import pandas as pd
import psycopg2
from urllib.parse import urlparse
import Registro,Historial,Capacitacion,Salir

def Bonos(usuario,puesto):

  # ----- Conexión, Botones y Memoria ---- #

  uri=st.secrets.db_credentials.URI
  result = urlparse(uri)
  hostname = result.hostname
  database = result.path[1:]
  username = result.username
  pwd = result.password
  port_id = result.port
  con = psycopg2.connect(host=hostname,dbname= database,user= username,password=pwd,port= port_id)

  placeholder1_9= st.sidebar.empty()
  titulo= placeholder1_9.title("Menú")

  placeholder2_9 = st.sidebar.empty()
  registro_9 = placeholder2_9.button("Registro",key="registro_9")

  placeholder3_9 = st.sidebar.empty()
  historial_9 = placeholder3_9.button("Historial",key="historial_9")

  placeholder4_9 = st.sidebar.empty()
  capacitacion_9= placeholder4_9.button("Capacitaciones",key="capacitacion_9")

  placeholder5_9 = st.sidebar.empty()
  salir_9 = placeholder5_9.button("Salir",key="salir_9")

  placeholder6_9 = st.empty()
  bonos_9 = placeholder6_9.title("Bonos")
  
  placeholder7_9 = st.empty()
  capacitacion_registro_9 = placeholder7_9.subheader("Sección No Disponible")

  # ----- Registro ---- #
    
  if registro_9:
    placeholder1_9.empty()
    placeholder2_9.empty()
    placeholder3_9.empty()
    placeholder4_9.empty()
    placeholder5_9.empty()   
    placeholder6_9.empty()
    placeholder7_9.empty()
    st.session_state.Registro=False
    st.session_state.Bonos=False

    perfil=pd.read_sql(f"select perfil from usuarios where usuario ='{usuario}'",uri)
    perfil= perfil.loc[0,'perfil']

    if perfil=="1":        
                    
      Registro.Registro1(usuario,puesto)
                
    elif perfil=="2":        
                    
      Registro.Registro2(usuario,puesto)   

    elif perfil=="3":  

      Registro.Registro3(usuario,puesto)       

  # ----- Historial ---- #
    
  elif historial_9:
    placeholder1_9.empty()
    placeholder2_9.empty()
    placeholder3_9.empty()
    placeholder4_9.empty()
    placeholder5_9.empty()   
    placeholder6_9.empty()
    placeholder7_9.empty()
    st.session_state.Bonos=False
    st.session_state.Historial=True
    Historial.Historial(usuario,puesto)

  # ----- Capacitación ---- #
    
  elif capacitacion_9:
    placeholder1_9.empty()
    placeholder2_9.empty()
    placeholder3_9.empty()
    placeholder4_9.empty()
    placeholder5_9.empty()   
    placeholder6_9.empty()
    placeholder7_9.empty()
    st.session_state.Bonos=False
    st.session_state.Capacitacion=True
    Capacitacion.Capacitacion(usuario,puesto)

  # ----- Salir ---- #
    
  elif salir_9:
    placeholder1_9.empty()
    placeholder2_9.empty()
    placeholder3_9.empty()
    placeholder4_9.empty()
    placeholder5_9.empty()   
    placeholder6_9.empty()
    placeholder7_9.empty()
    st.session_state.Ingreso = False
    st.session_state.Bonos=False
    st.session_state.Salir=True
    Salir.Salir()