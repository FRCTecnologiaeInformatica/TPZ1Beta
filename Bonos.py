# ----- Librerías ---- #

import streamlit as st
import pandas as pd
import psycopg2
from urllib.parse import urlparse
import Procesos,Historial,Capacitacion,Otros_Registros,Salir

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
  procesos_9 = placeholder2_9.button("Procesos",key="procesos_9")

  placeholder3_9 = st.sidebar.empty()
  historial_9 = placeholder3_9.button("Historial",key="historial_9")

  placeholder4_9 = st.sidebar.empty()
  capacitacion_9= placeholder4_9.button("Capacitaciones",key="capacitacion_9")

  placeholder5_9 = st.sidebar.empty()
  otros_registros_9= placeholder5_9.button("Otros Registros",key="otros_registros_9")

  placeholder6_9 = st.sidebar.empty()
  salir_9 = placeholder6_9.button("Salir",key="salir_9")

  placeholder7_9 = st.empty()
  bonos_9 = placeholder7_9.title("Bonos")
  
  placeholder8_9 = st.empty()
  capacitacion_registro_8 = placeholder7_9.subheader("Sección No Disponible")

  # ----- Procesos ---- #
    
  if procesos_9:
    placeholder1_9.empty()
    placeholder2_9.empty()
    placeholder3_9.empty()
    placeholder4_9.empty()
    placeholder5_9.empty()   
    placeholder6_9.empty()
    placeholder7_9.empty()
    placeholder8_9.empty()
    st.session_state.Procesos=False
    st.session_state.Bonos=False

    perfil=pd.read_sql(f"select perfil from usuarios where usuario ='{usuario}'",uri)
    perfil= perfil.loc[0,'perfil']

    if perfil=="1":        
                    
      Procesos.Procesos1(usuario,puesto)
                
    elif perfil=="2":        
                    
      Procesos.Procesos2(usuario,puesto)   

    elif perfil=="3":  

      Procesos.Procesos3(usuario,puesto)       

  # ----- Historial ---- #
    
  elif historial_9:
    placeholder1_9.empty()
    placeholder2_9.empty()
    placeholder3_9.empty()
    placeholder4_9.empty()
    placeholder5_9.empty()   
    placeholder6_9.empty()
    placeholder7_9.empty()
    placeholder8_9.empty()
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
    placeholder8_9.empty()
    st.session_state.Bonos=False
    st.session_state.Capacitacion=True
    Capacitacion.Capacitacion(usuario,puesto)

  # ----- Otros Registros ---- #
    
  elif otros_registros_9:
    placeholder1_9.empty()
    placeholder2_9.empty()
    placeholder3_9.empty()
    placeholder4_9.empty()
    placeholder5_9.empty()   
    placeholder6_9.empty()
    placeholder7_9.empty()
    placeholder8_9.empty()
    st.session_state.Bonos=False
    st.session_state.Otros_Registros=True
    Otros_Registros.Otros_Registros(usuario,puesto)

  # ----- Salir ---- #
    
  elif salir_9:
    placeholder1_9.empty()
    placeholder2_9.empty()
    placeholder3_9.empty()
    placeholder4_9.empty()
    placeholder5_9.empty()   
    placeholder6_9.empty()
    placeholder7_9.empty()
    placeholder8_9.empty()
    st.session_state.Ingreso = False
    st.session_state.Bonos=False
    st.session_state.Salir=True
    Salir.Salir()