# ----- Librerías ---- #
import numpy as np
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

  # ----- Datos Supervisor y Coordinador ---- #

  if puesto=="Supervisor" or puesto=="Coordinador":      

    placeholder9_7 = st.empty()
    filtro_7 = placeholder9_7.selectbox("Filtro", options=("Todos","Operarios","Propio","Personal Asignado"), key="filtro_7")

    placeholder10_7 = st.empty()
    proceso_7_s = placeholder10_7.selectbox("Proceso", options=("Todos","Conformación","Control de Calidad Conformación","Información Final I","Control de Calidad IF I","Información Final II","Información Final III"), key="proceso_7_s")
    
    placeholder11_7 = st.empty()
    tipo_7_s = placeholder11_7.selectbox("Tipo", options=("Ordinario","Corrección"), key="tipo_7_s")

    if filtro_7=="Todos" and proceso_7_s=="Todos":
        
        data_1=pd.read_sql(f"select marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where tipo='{tipo_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
        data_2 = data_1.groupby(["nombre", "fecha"], as_index=False)["predios","horas"].agg(np.sum)
        data_3 = data_1.groupby(["fecha"], as_index=False)["predios"].agg(np.sum)

    elif filtro_7=="Todos" and proceso_7_s !="Todos":
        
        data_1=pd.read_sql(f"select marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where proceso='{proceso_7_s}' and tipo='{tipo_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
        data_2 = data_1.groupby(["nombre", "fecha"], as_index=False)["predios","horas"].agg(np.sum)
        data_3 = data_1.groupby(["fecha"], as_index=False)["predios"].agg(np.sum)

    elif filtro_7=="Operarios" and proceso_7_s =="Todos":
       
        data_1=pd.read_sql(f"select marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where puesto='Operario Catastral' and tipo='{tipo_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
        data_2 = data_1.groupby(["nombre", "fecha"], as_index=False)["predios","horas"].agg(np.sum)
        data_3 = data_1.groupby(["fecha"], as_index=False)["predios"].agg(np.sum)

    elif filtro_7=="Operarios" and proceso_7_s !="Todos":
        
        data_1=pd.read_sql(f"select marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where puesto='Operario Catastral' and tipo='{tipo_7_s}' and proceso='{proceso_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
        data_2 = data_1.groupby(["nombre", "fecha"], as_index=False)["predios","horas"].agg(np.sum)
        data_3 = data_1.groupby(["fecha"], as_index=False)["predios"].agg(np.sum)

    elif filtro_7=="Propio" and proceso_7_s=="Todos":
        
        data_1=pd.read_sql(f"select marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where usuario='{usuario}' and tipo='{tipo_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
        data_2 = data_1.groupby(["nombre", "fecha"], as_index=False)["predios","horas"].agg(np.sum)
        data_3 = data_1.groupby(["fecha"], as_index=False)["predios"].agg(np.sum)

    elif filtro_7=="Propio" and proceso_7_s !="Todos":
        
        data_1=pd.read_sql(f"select marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where usuario='{usuario}' and tipo='{tipo_7_s}' and proceso='{proceso_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
        data_2 = data_1.groupby(["nombre", "fecha"], as_index=False)["predios","horas"].agg(np.sum)
        data_3 = data_1.groupby(["fecha"], as_index=False)["predios"].agg(np.sum)

    elif filtro_7=="Personal Asignado" and proceso_7_s =="Todos":
        
        data_1=pd.read_sql(f"select marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where supervisor='{nombre_7}' and tipo='{tipo_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
        data_2 = data_1.groupby(["nombre", "fecha"], as_index=False)["predios","horas"].agg(np.sum)
        data_3 = data_1.groupby(["fecha"], as_index=False)["predios"].agg(np.sum)

    elif filtro_7=="Personal Asignado" and proceso_7_s !="Todos":
       
        data_1=pd.read_sql(f"select marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where supervisor='{nombre_7}' and tipo='{tipo_7_s}' and proceso='{proceso_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
        data_2 = data_1.groupby(["nombre", "fecha"], as_index=False)["predios","horas"].agg(np.sum)
        data_3 = data_1.groupby(["fecha"], as_index=False)["predios"].agg(np.sum)

  # ----- Datos Operario Catastral ---- #

  elif puesto=="Operario Catastral":

    placeholder12_7 = st.empty()
    proceso_7_o= placeholder12_7.selectbox("Proceso", options=("Todos","Conformación","Control de Calidad Conformación","Información Final I","Control de Calidad IF I","Información Final II","Información Final III"), key="proceso_7_o")

    placeholder13_7 = st.empty()
    tipo_7_o = placeholder13_7.selectbox("Tipo", options=("Ordinario","Corrección"), key="tipo_7_o")    

    if proceso_7_o =="Todos":
        
      data_1=pd.read_sql(f"select marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where usuario='{usuario}' and tipo='{tipo_7_o}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2 = data_1.groupby(["nombre", "fecha"], as_index=False)["predios","horas"].agg(np.sum)

    else:
       
      data_1=pd.read_sql(f"select marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where usuario='{usuario}'and tipo='{tipo_7_o}' and proceso='{proceso_7_o}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2 = data_1.groupby(["nombre", "fecha"], as_index=False)["predios","horas"].agg(np.sum)

  # ----- Reportes ---- #
  
  placeholder14_7 = st.empty()
  reportes_7=placeholder14_7.subheader("Reportes")   

  placeholder15_7 = st.empty()
  historial_7_data_1=placeholder15_7.dataframe(data=data_1)

  placeholder16_7 = st.empty()
  descarga_7_data_1 = placeholder16_7.download_button("Decargar CSV",data=data_1.to_csv(),mime="text/csv",key="descarga_7_data_1")

  # ----- Resumen ---- #

  placeholder17_7 = st.empty()
  resumen_7=placeholder17_7.subheader("Resumen")  

  placeholder18_7 = st.empty()
  historial_7_data_2= placeholder18_7.dataframe(data=data_2)

  placeholder19_7 = st.empty()
  descarga_7_data_2 = placeholder19_7.download_button("Decargar CSV",data=data_2.to_csv(),mime="text/csv",key="descarga_7_data_2")

  nombre_7_2=data_2.iloc[:,0]
  pivot=len(nombre_7_2)

  if pivot==0:

    st.error('No existen datos para mostrar')

  else:
    fecha_7_2=data_2.iloc[:,1]
    predio_7_2=data_2.iloc[:,2]
    d = {'col1':nombre_7_2, 'col2':fecha_7_2,'col3':predio_7_2 }
    df = pd.DataFrame(data=d)
    lista_nombres_7_2 = df["col1"].unique().tolist()

    placeholder20_7 = st.empty()
    nombres= placeholder20_7.multiselect("Seleccionar",lista_nombres_7_2)

    dfs = {nombre: df[df["col1"] == nombre] for nombre in nombres}
    fig_2 = go.Figure()
    for nombre, df in dfs.items():
      fig_2 = fig_2.add_trace(go.Scatter(x=df["col2"], y=df["col3"], name=nombre))

    placeholder21_7 = st.empty()
    grafico_7_2= placeholder21_7.plotly_chart(fig_2)

    # ----- Total ---- #

    if puesto=="Supervisor" or puesto=="Coordinador":

      placeholder22_7 = st.empty()
      total_7=placeholder22_7.subheader("Total")  
        
      fig_3 = px.bar(data_3, x="fecha", y="predios", text="predios")
      fig_3.update_traces(textposition="outside")
      placeholder23_7 = st.empty()
      grafico_7_3= placeholder23_7.plotly_chart(fig_3)

      placeholder24_7 = st.empty()
      descarga_7_data_3 = placeholder24_7.download_button("Decargar CSV",data=data_3.to_csv(),mime="text/csv",key="descarga_7_data_3")

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
      placeholder11_7.empty()
    elif puesto=="Operario Catastral": 
      placeholder12_7.empty()
      placeholder13_7.empty()
    placeholder14_7.empty()
    placeholder15_7.empty()
    placeholder16_7.empty()
    placeholder17_7.empty()
    placeholder18_7.empty()
    placeholder19_7.empty()
    if pivot!=0 and puesto=="Operario Catastral": 
      placeholder20_7.empty()
      placeholder21_7.empty()
    elif pivot!=0 and puesto=="Supervisor" or puesto=="Coordinador":
      placeholder20_7.empty()
      placeholder21_7.empty()
      placeholder22_7.empty()
      placeholder23_7.empty()
      placeholder24_7.empty()
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
      placeholder11_7.empty()
    elif puesto=="Operario Catastral": 
      placeholder12_7.empty()
      placeholder13_7.empty()
    placeholder14_7.empty()
    placeholder15_7.empty()
    placeholder16_7.empty()
    placeholder17_7.empty()
    placeholder18_7.empty()
    placeholder19_7.empty()
    if pivot!=0 and puesto=="Operario Catastral": 
      placeholder20_7.empty()
      placeholder21_7.empty()
    elif pivot!=0 and puesto=="Supervisor" or puesto=="Coordinador":
      placeholder20_7.empty()
      placeholder21_7.empty()
      placeholder22_7.empty()
      placeholder23_7.empty()
      placeholder24_7.empty()
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
      placeholder11_7.empty()
    elif puesto=="Operario Catastral": 
      placeholder12_7.empty()
      placeholder13_7.empty()
    placeholder14_7.empty()
    placeholder15_7.empty()
    placeholder16_7.empty()
    placeholder17_7.empty()
    placeholder18_7.empty()
    placeholder19_7.empty()
    if pivot!=0 and puesto=="Operario Catastral": 
      placeholder20_7.empty()
      placeholder21_7.empty()
    elif pivot!=0 and puesto=="Supervisor" or puesto=="Coordinador":
      placeholder20_7.empty()
      placeholder21_7.empty()
      placeholder22_7.empty()
      placeholder23_7.empty()
      placeholder24_7.empty()
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
      placeholder11_7.empty()
    elif puesto=="Operario Catastral": 
      placeholder12_7.empty()
      placeholder13_7.empty()
    placeholder14_7.empty()
    placeholder15_7.empty()
    placeholder16_7.empty()
    placeholder17_7.empty()
    placeholder18_7.empty()
    placeholder19_7.empty()
    if pivot!=0 and puesto=="Operario Catastral": 
      placeholder20_7.empty()
      placeholder21_7.empty()
    elif pivot!=0 and puesto=="Supervisor" or puesto=="Coordinador":
      placeholder20_7.empty()
      placeholder21_7.empty()
      placeholder22_7.empty()
      placeholder23_7.empty()
      placeholder24_7.empty()
    st.session_state.Ingreso = False
    st.session_state.Historial=False
    st.session_state.Salir=True
    Salir.Salir()