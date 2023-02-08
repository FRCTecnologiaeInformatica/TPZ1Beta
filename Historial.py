# ----- Librerías ---- #

import streamlit as st
import pandas as pd
import psycopg2
import plotly.graph_objects as go
import plotly.express as px
from urllib.parse import urlparse
uri=st.secrets.db_credentials.URI
import Registro,Capacitacion,Bonos,Salir

def Historial(usuario,puesto):

  # ----- Conexión, Botones y Memoria ---- #

  uri=st.secrets.db_credentials.URI
  result = urlparse(uri)
  hostname = result.hostname
  database = result.path[1:]
  username = result.username
  pwd = result.password
  port_id = result.port
  con = psycopg2.connect(host=hostname,dbname= database,user= username,password=pwd,port= port_id)

  placeholder1_7= st.sidebar.empty()
  titulo= placeholder1_7.title("Menú")

  placeholder2_7 = st.sidebar.empty()
  registro_7 = placeholder2_7.button("Registro",key="registro_7")

  placeholder3_7 = st.sidebar.empty()
  capacitacion_7 = placeholder3_7.button("Capacitaciones",key="capacitacion_7")

  placeholder4_7 = st.sidebar.empty()
  bonos_7 = placeholder4_7.button("Bonos",key="bonos_7")

  placeholder5_7 = st.sidebar.empty()
  salir_7 = placeholder5_7.button("Salir",key="salir_7")

  placeholder6_7 = st.empty()
  historial_7 = placeholder6_7.title("Historial")

  placeholder7_7 = st.empty()
  fecha_de__inicio_7 = placeholder7_7.date_input("Fecha de Inicio",key="fecha_de_inicio_7")

  placeholder8_7 = st.empty()
  fecha_de__finalizacion_7 = placeholder8_7.date_input("Fecha de Finalización",key="fecha_de_finalizacion_7")
  
  nombre_7= pd.read_sql(f"select nombre from usuarios where usuario ='{usuario}'",uri)
  nombre_7 = nombre_7.loc[0,'nombre']

  if puesto=="Supervisor" or puesto=="Coordinador":      

    placeholder9_7 = st.empty()
    filtro_7 = placeholder9_7.selectbox("Filtro", options=("Todos","Operarios","Propio","Personal Asignado"), key="filtro_7")

    placeholder10_7 = st.empty()
    proceso_7_s = placeholder10_7.selectbox("Proceso", options=("Todos","Conformación","Control de Calidad Conformación","Información Final I","Control de Calidad IFI","Información Final II","Información Final III"), key="proceso_7_s")
    
    if filtro_7=="Todos" and proceso_7_s=="Todos":
        data = pd.read_sql(f"select marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,predios,horas from registro where fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
    
    elif filtro_7=="Todos" and proceso_7_s !="Todos":
        data = pd.read_sql(f"select marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,predios,horas from registro where proceso='{proceso_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      
    elif filtro_7=="Operarios" and proceso_7_s =="Todos":
        data = pd.read_sql(f"select marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,predios,horas from registro where puesto='Operario Catastral' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
    
    elif filtro_7=="Operarios" and proceso_7_s !="Todos":
        data = pd.read_sql(f"select marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,predios,horas from registro where puesto='Operario Catastral' and proceso='{proceso_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
    
    elif filtro_7=="Propio" and proceso_7_s =="Todos":
        data = pd.read_sql(f"select marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,predios,horas from registro where usuario='{usuario}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)

    elif filtro_7=="Propio" and proceso_7_s !="Todos":
        data = pd.read_sql(f"select marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,predios,horas from registro where usuario='{usuario}' and proceso='{proceso_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)

    elif filtro_7=="Personal Asignado" and proceso_7_s =="Todos":
        data = pd.read_sql(f"select marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,predios,horas from registro where supervisor='{nombre_7}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)

    elif filtro_7=="Personal Asignado" and proceso_7_s !="Todos":
        data = pd.read_sql(f"select marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,predios,horas from registro where supervisor='{nombre_7}' and proceso='{proceso_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)

  elif puesto=="Operario Catastral":

    placeholder11_7 = st.empty()
    proceso_7_o= placeholder11_7.selectbox("Proceso", options=("Todos","Conformación","Control de Calidad Conformación","Información Final I","Control de Calidad IFI","Información Final II","Información Final III"), key="proceso_7_o")
        
    if proceso_7_o =="Todos":
        data = pd.read_sql(f"select marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,predios,horas from registro where usuario='{usuario}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)

    else:
        data = pd.read_sql(f"select marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,predios,horas from registro where usuario='{usuario}'and proceso='{proceso_7_o}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)

  placeholder12_7 = st.empty()
  historial_7= placeholder12_7.dataframe(data=data)

  placeholder13_7 = st.empty()
  descarga_7 = placeholder13_7.download_button("Decargar CSV",data=data.to_csv(),mime="text/csv",key="descarga_7")

  nombre_7=data.iloc[:,2]
  fecha_7=data.iloc[:,7]
  predio_7=data.iloc[:,11]
  d = {'col1':nombre_7, 'col2':fecha_7,'col3':predio_7 }
  df = pd.DataFrame(data=d)
  lista_nombres_7 = df["col1"].unique().tolist()

  placeholder14_7 = st.empty()
  nombres= placeholder14_7.multiselect("Seleccionar",lista_nombres_7)

  dfs = {nombre: df[df["col1"] == nombre] for nombre in nombres}
  fig = go.Figure()
  for nombre, df in dfs.items():
    fig = fig.add_trace(go.Scatter(x=df["col2"], y=df["col3"], name=nombre))

  placeholder15_7 = st.empty()
  historial_15= placeholder15_7.plotly_chart(fig)

  # ----- Registro ---- #
    
  if registro_7:
    placeholder1_7.empty()
    placeholder2_7.empty()
    placeholder3_7.empty()
    placeholder4_7.empty()
    placeholder5_7.empty()   
    placeholder6_7.empty()
    placeholder7_7.empty()
    placeholder8_7.empty()
    if puesto=="Supervisor" or puesto=="Coordinador":  
      placeholder9_7.empty()
      placeholder10_7.empty()
    elif puesto=="Operario Catastral": 
      placeholder11_7.empty()
    placeholder12_7.empty()
    placeholder13_7.empty()
    placeholder14_7.empty()
    placeholder15_7.empty()
    st.session_state.Registro=False
    st.session_state.Historial=False

    perfil=pd.read_sql(f"select perfil from usuarios where usuario ='{usuario}'",uri)
    perfil= perfil.loc[0,'perfil']

    if perfil=="1":        
                    
      Registro.Registro1(usuario,puesto)
                
    elif perfil=="2":        
                    
      Registro.Registro2(usuario,puesto)   

    elif perfil=="3":  

      Registro.Registro3(usuario,puesto)       


  # ----- Capacitación ---- #
    
  elif capacitacion_7:
    placeholder1_7.empty()
    placeholder2_7.empty()
    placeholder3_7.empty()
    placeholder4_7.empty()
    placeholder5_7.empty()   
    placeholder6_7.empty()
    placeholder7_7.empty()
    placeholder8_7.empty()
    if puesto=="Supervisor" or puesto=="Coordinador":  
      placeholder9_7.empty()
      placeholder10_7.empty()
    elif puesto=="Operario Catastral": 
      placeholder11_7.empty()
    placeholder12_7.empty()
    placeholder13_7.empty()
    placeholder14_7.empty()
    placeholder15_7.empty()
    st.session_state.Historial=False
    st.session_state.Capacitacion=True
    Capacitacion.Capacitacion(usuario,puesto)

      # ----- Bonos ---- #
    
  elif bonos_7:
    placeholder1_7.empty()
    placeholder2_7.empty()
    placeholder3_7.empty()
    placeholder4_7.empty()
    placeholder5_7.empty()   
    placeholder6_7.empty()
    placeholder7_7.empty()
    placeholder8_7.empty()
    if puesto=="Supervisor" or puesto=="Coordinador":  
      placeholder9_7.empty()
      placeholder10_7.empty()
    elif puesto=="Operario Catastral": 
      placeholder11_7.empty()
    placeholder12_7.empty()
    placeholder13_7.empty()
    placeholder14_7.empty()
    placeholder15_7.empty()
    st.session_state.Historial=False
    st.session_state.Bonos=True
    Bonos.Bonos(usuario,puesto)
    
    # ----- Salir ---- #
    
  elif salir_7:
    placeholder1_7.empty()
    placeholder2_7.empty()
    placeholder3_7.empty()
    placeholder4_7.empty()
    placeholder5_7.empty()   
    placeholder6_7.empty()
    placeholder7_7.empty()
    placeholder8_7.empty()
    if puesto=="Supervisor" or puesto=="Coordinador":  
      placeholder9_7.empty()
      placeholder10_7.empty()
    elif puesto=="Operario Catastral": 
      placeholder11_7.empty()
    placeholder12_7.empty()
    placeholder13_7.empty()
    placeholder14_7.empty()
    placeholder15_7.empty()
    st.session_state.Ingreso = False
    st.session_state.Historial=False
    st.session_state.Salir=True
    Salir.Salir()