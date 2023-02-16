# ----- Librerías ---- #

import streamlit as st
import pandas as pd
import psycopg2
from datetime import datetime
import pytz
from urllib.parse import urlparse
import Registro,Historial,Capacitacion,Bonos,Salir

def IFI(usuario,puesto):

  # ----- Conexión, Botones y Memoria ---- #

  uri=st.secrets.db_credentials.URI
  result = urlparse(uri)
  hostname = result.hostname
  database = result.path[1:]
  username = result.username
  pwd = result.password
  port_id = result.port
  con = psycopg2.connect(host=hostname,dbname= database,user= username,password=pwd,port= port_id)

  placeholder1_3= st.sidebar.empty()
  titulo= placeholder1_3.title("Menú")

  placeholder2_3 = st.sidebar.empty()
  registro_3 = placeholder2_3.button("Registro",key="registro_3")

  placeholder3_3 = st.sidebar.empty()
  historial_3 = placeholder3_3.button("Historial",key="historial_3")

  placeholder4_3 = st.sidebar.empty()
  capacitacion_3 = placeholder4_3.button("Capacitaciones",key="capacitacion_3")

  placeholder5_3 = st.sidebar.empty()
  bonos_3 = placeholder5_3.button("Bonos",key="bonos_3")

  placeholder6_3 = st.sidebar.empty()
  salir_3 = placeholder6_3.button("Salir",key="salir_3")

  placeholder7_3 = st.empty()
  informacion_final_i_3 = placeholder7_3.title("Información Final I")

  default_date = datetime.now(pytz.timezone('America/Chicago'))

  placeholder8_3= st.empty()
  fecha_3= placeholder8_3.date_input("Fecha",value=default_date,key="fecha_3")

  placeholder9_3= st.empty()
  bloque_3= placeholder9_3.number_input("Bloque",min_value=10000000,max_value=99999999,step=1,key="bloque_3")
    
  placeholder10_3= st.empty()
  estado_3= placeholder10_3.selectbox("Estado", options=("En Proceso","Conflicto","Terminado"), key="estado_3")
       
  placeholder11_3= st.empty()
  tipo_3= placeholder11_3.selectbox("Tipo", options=("Ordinario","Corrección"), key="tipo_3")

  placeholder12_3= st.empty()
  predios_3= placeholder12_3.number_input("Cantidad de Predios Producidos",min_value=0,step=1,key="predios_3")

  placeholder13_3= st.empty()
  horas_3= placeholder13_3.number_input("Cantidad de Horas Trabajadas en el Proceso",min_value=0.0,key="horas_3")

  placeholder14_3 = st.empty()
  reporte_3 = placeholder14_3.button("Generar Reporte",key="reporte_3")

  # ----- Registro ---- #
    
  if registro_3:
    placeholder1_3.empty()
    placeholder2_3.empty()
    placeholder3_3.empty()
    placeholder4_3.empty()
    placeholder5_3.empty()
    placeholder6_3.empty()
    placeholder7_3.empty()
    placeholder8_3.empty()
    placeholder9_3.empty()
    placeholder10_3.empty()
    placeholder11_3.empty()
    placeholder12_3.empty()
    placeholder13_3.empty()
    placeholder14_3.empty()
    st.session_state.Registro=False
    st.session_state.IFI=False

    perfil=pd.read_sql(f"select perfil from usuarios where usuario ='{usuario}'",uri)
    perfil= perfil.loc[0,'perfil']

    if perfil=="1":        
                    
      Registro.Registro1(usuario,puesto)
                
    elif perfil=="2":        
                    
      Registro.Registro2(usuario,puesto)   

    elif perfil=="3":  

      Registro.Registro3(usuario,puesto)       


  #----- Historial ---- #
    
  elif historial_3:
    placeholder1_3.empty()
    placeholder2_3.empty()
    placeholder3_3.empty()
    placeholder4_3.empty()
    placeholder5_3.empty()
    placeholder6_3.empty()
    placeholder7_3.empty()
    placeholder8_3.empty()
    placeholder9_3.empty()
    placeholder10_3.empty()
    placeholder11_3.empty()
    placeholder12_3.empty()
    placeholder13_3.empty()
    placeholder14_3.empty()
    st.session_state.IFI=False
    st.session_state.Historial=True
    Historial.Historial(usuario,puesto)   

  # ----- Capacitación ---- #
    
  elif capacitacion_3:
    placeholder1_3.empty()
    placeholder2_3.empty()
    placeholder3_3.empty()
    placeholder4_3.empty()
    placeholder5_3.empty()
    placeholder6_3.empty()
    placeholder7_3.empty()
    placeholder8_3.empty()
    placeholder9_3.empty()
    placeholder10_3.empty()
    placeholder11_3.empty()
    placeholder12_3.empty()
    placeholder13_3.empty()
    placeholder14_3.empty()
    st.session_state.IFI=False
    st.session_state.Capacitacion=True
    Capacitacion.Capacitacion(usuario,puesto)

  # ----- Bonos ---- #
    
  elif bonos_3:
    placeholder1_3.empty()
    placeholder2_3.empty()
    placeholder3_3.empty()
    placeholder4_3.empty()
    placeholder5_3.empty()
    placeholder6_3.empty()
    placeholder7_3.empty()
    placeholder8_3.empty()
    placeholder9_3.empty()
    placeholder10_3.empty()
    placeholder11_3.empty()
    placeholder12_3.empty()
    placeholder13_3.empty()
    placeholder14_3.empty()
    st.session_state.IFI=False
    st.session_state.Bonos=True
    Bonos.Bonos(usuario,puesto)    

    # ----- Salir ---- #
    
  elif salir_3:
    placeholder1_3.empty()
    placeholder2_3.empty()
    placeholder3_3.empty()
    placeholder4_3.empty()
    placeholder5_3.empty()
    placeholder6_3.empty()
    placeholder7_3.empty()
    placeholder8_3.empty()
    placeholder9_3.empty()
    placeholder10_3.empty()
    placeholder11_3.empty()
    placeholder12_3.empty()
    placeholder13_3.empty()
    placeholder14_3.empty()
    st.session_state.Ingreso = False
    st.session_state.IFI=False
    st.session_state.Salir=True
    Salir.Salir()

  elif reporte_3:

    cursor01=con.cursor()

    marca_3= datetime.now(pytz.timezone('America/Chicago')).strftime("%Y-%m-%d %H:%M:%S")
    
    nombre_3= pd.read_sql(f"select nombre from usuarios where usuario ='{usuario}'",uri)
    nombre_3 = nombre_3.loc[0,'nombre']
      
    horario_3= pd.read_sql(f"select horario from usuarios where usuario ='{usuario}'",uri)
    horario_3 = horario_3.loc[0,'horario']

    supervisor_3= pd.read_sql(f"select supervisor from usuarios where usuario ='{usuario}'",uri)
    supervisor_3 = supervisor_3.loc[0,'supervisor']

    cursor01.execute(f"INSERT INTO registro (marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,predios,horas)VALUES('{marca_3}','{usuario}','{nombre_3}','{horario_3}','{puesto}','{supervisor_3}','Información Final I','{fecha_3}','{bloque_3}','{estado_3}','{tipo_3}','{predios_3}','{horas_3}')")
    con.commit()                                                                                                                                 
    st.success('Registro enviado correctamente')