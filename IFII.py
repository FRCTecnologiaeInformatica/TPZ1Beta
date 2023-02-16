# ----- Librerías ---- #

import streamlit as st
import pandas as pd
import psycopg2
from datetime import datetime
import pytz
from urllib.parse import urlparse
import Registro,Historial,Capacitacion,Bonos,Salir

def IFII(usuario,puesto):

  # ----- Conexión, Botones y Memoria ---- #

  uri=st.secrets.db_credentials.URI
  result = urlparse(uri)
  hostname = result.hostname
  database = result.path[1:]
  username = result.username
  pwd = result.password
  port_id = result.port
  con = psycopg2.connect(host=hostname,dbname= database,user= username,password=pwd,port= port_id)

  placeholder1_4= st.sidebar.empty()
  titulo= placeholder1_4.title("Menú")

  placeholder2_4 = st.sidebar.empty()
  registro_4 = placeholder2_4.button("Registro",key="registro_4")

  placeholder3_4 = st.sidebar.empty()
  historial_4 = placeholder3_4.button("Historial",key="historial_4")

  placeholder4_4 = st.sidebar.empty()
  capacitacion_4 = placeholder4_4.button("Capacitaciones",key="capacitacion_4")

  placeholder5_4 = st.sidebar.empty()
  bonos_4 = placeholder5_4.button("Bonos",key="bonos_4")

  placeholder6_4 = st.sidebar.empty()
  salir_4 = placeholder6_4.button("Salir",key="salir_4")

  placeholder7_4 = st.empty()
  informacion_final_ii_4 = placeholder7_4.title("Información Final II")

  default_date = datetime.now(pytz.timezone('America/Chicago'))

  placeholder8_4= st.empty()
  fecha_4= placeholder8_4.date_input("Fecha",value=default_date,key="fecha_4")

  placeholder9_4= st.empty()
  bloque_4= placeholder9_4.number_input("Bloque o Distrito",min_value=10000000,max_value=99999999,step=1,key="bloque_4")
    
  placeholder10_4= st.empty()
  tipo_4= placeholder10_4.selectbox("Estado", options=("En Proceso","Conflicto","Terminado"), key="estado_4")
       
  placeholder11_4= st.empty()
  estado_4= placeholder11_4.selectbox("Tipo", options=("Ordinario","Corrección"), key="tipo_4")

  placeholder12_4= st.empty()
  predios_4= placeholder12_4.number_input("Cantidad de Predios Producidos",min_value=0,step=1,key="predios_4")

  placeholder13_4= st.empty()
  horas_4= placeholder13_4.number_input("Cantidad de Horas Trabajadas en el Proceso",min_value=0.0,key="horas_4")

  placeholder14_4 = st.empty()
  reporte_4 = placeholder14_4.button("Generar Reporte",key="reporte_4")

  # ----- Registro ---- #
    
  if registro_4:
    placeholder1_4.empty()
    placeholder2_4.empty()
    placeholder3_4.empty()
    placeholder4_4.empty()
    placeholder5_4.empty()
    placeholder6_4.empty()
    placeholder7_4.empty()
    placeholder8_4.empty()
    placeholder9_4.empty()
    placeholder10_4.empty()
    placeholder11_4.empty()
    placeholder12_4.empty()
    placeholder13_4.empty()
    placeholder14_4.empty()
    st.session_state.Registro=False
    st.session_state.IFII=False

    perfil=pd.read_sql(f"select perfil from usuarios where usuario ='{usuario}'",uri)
    perfil= perfil.loc[0,'perfil']

    if perfil=="1":        
                    
      Registro.Registro1(usuario,puesto)
                
    elif perfil=="2":        
                    
      Registro.Registro2(usuario,puesto)   

    elif perfil=="3":  

      Registro.Registro3(usuario,puesto)       

  #----- Historial ---- #
    
  elif historial_4:
    placeholder1_4.empty()
    placeholder2_4.empty()
    placeholder3_4.empty()
    placeholder4_4.empty()
    placeholder5_4.empty()
    placeholder6_4.empty()
    placeholder7_4.empty()
    placeholder8_4.empty()
    placeholder9_4.empty()
    placeholder10_4.empty()
    placeholder11_4.empty()
    placeholder12_4.empty()
    placeholder13_4.empty()
    placeholder14_4.empty()
    st.session_state.IFII=False
    st.session_state.Historial=True
    Historial.Historial(usuario,puesto)   

  # ----- Capacitación ---- #
    
  elif capacitacion_4:
    placeholder1_4.empty()
    placeholder2_4.empty()
    placeholder3_4.empty()
    placeholder4_4.empty()
    placeholder5_4.empty()
    placeholder6_4.empty()
    placeholder7_4.empty()
    placeholder8_4.empty()
    placeholder9_4.empty()
    placeholder10_4.empty()
    placeholder11_4.empty()
    placeholder12_4.empty()
    placeholder13_4.empty()
    placeholder14_4.empty()
    st.session_state.IFII=False
    st.session_state.Capacitacion=True
    Capacitacion.Capacitacion(usuario,puesto)

  # ----- Bonos ---- #
    
  elif bonos_4:
    placeholder1_4.empty()
    placeholder2_4.empty()
    placeholder3_4.empty()
    placeholder4_4.empty()
    placeholder5_4.empty()
    placeholder6_4.empty()
    placeholder7_4.empty()
    placeholder8_4.empty()
    placeholder9_4.empty()
    placeholder10_4.empty()
    placeholder11_4.empty()
    placeholder12_4.empty()
    placeholder13_4.empty()
    placeholder14_4.empty()
    st.session_state.IFII=False
    st.session_state.Bonos=True
    Bonos.Bonos(usuario,puesto)
    
    # ----- Salir ---- #
    
  elif salir_4:
    placeholder1_4.empty()
    placeholder2_4.empty()
    placeholder3_4.empty()
    placeholder4_4.empty()
    placeholder5_4.empty()
    placeholder6_4.empty()
    placeholder7_4.empty()
    placeholder8_4.empty()
    placeholder9_4.empty()
    placeholder10_4.empty()
    placeholder11_4.empty()
    placeholder12_4.empty()
    placeholder13_4.empty()
    placeholder14_4.empty()
    st.session_state.Ingreso = False
    st.session_state.IFII=False
    st.session_state.Salir=True
    Salir.Salir()

  elif reporte_4:

    cursor01=con.cursor()

    marca_4= datetime.now(pytz.timezone('America/Chicago')).strftime("%Y-%m-%d %H:%M:%S")
    
    nombre_4= pd.read_sql(f"select nombre from usuarios where usuario ='{usuario}'",uri)
    nombre_4 = nombre_4.loc[0,'nombre']
      
    horario_4= pd.read_sql(f"select horario from usuarios where usuario ='{usuario}'",uri)
    horario_4= horario_4.loc[0,'horario']

    supervisor_4= pd.read_sql(f"select supervisor from usuarios where usuario ='{usuario}'",uri)
    supervisor_4 = supervisor_4.loc[0,'supervisor']

    cursor01.execute(f"INSERT INTO registro (marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,predios,horas)VALUES('{marca_4}','{usuario}','{nombre_4}','{horario_4}','{puesto}','{supervisor_4}','Información Final II','{fecha_4}','{bloque_4}','{estado_4}','{tipo_4}','{predios_4}','{horas_4}')")
    con.commit()
    st.success('Registro enviado correctamente')