# ----- Librerías ---- #
import numpy as np
import streamlit as st
import pandas as pd
import psycopg2
from datetime import datetime
import pytz
import plotly.graph_objects as go
import plotly.express as px
from urllib.parse import urlparse
uri=st.secrets.db_credentials.URI
import Procesos,Capacitacion,Otros_Registros,Bonos,Salir

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
  procesos_7 = placeholder2_7.button("Procesos",key="procesos_7")

  placeholder3_7 = st.sidebar.empty()
  capacitacion_7 = placeholder3_7.button("Capacitaciones",key="capacitacion_7")

  placeholder4_7 = st.sidebar.empty()
  otros_registros_7 = placeholder4_7.button("Otros Procesos",key="otros_registros_7")

  placeholder5_7 = st.sidebar.empty()
  bonos_7 = placeholder5_7.button("Bonos",key="bonos_7")

  placeholder6_7 = st.sidebar.empty()
  salir_7 = placeholder6_7.button("Salir",key="salir_7")

  placeholder7_7 = st.empty()
  historial_7 = placeholder7_7.title("Historial")

  default_date_7 = datetime.now(pytz.timezone('America/Chicago'))

  placeholder8_7 = st.empty()
  fecha_de__inicio_7 = placeholder8_7.date_input("Fecha de Inicio",value=default_date_7,key="fecha_de_inicio_7")

  placeholder9_7 = st.empty()
  fecha_de__finalizacion_7 = placeholder9_7.date_input("Fecha de Finalización",value=default_date_7,key="fecha_de_finalizacion_7")
  
  nombre_7= pd.read_sql(f"select nombre from usuarios where usuario ='{usuario}'",uri)
  nombre_7 = nombre_7.loc[0,'nombre']

  # ----- Datos Supervisor y Coordinador ---- #

  if puesto=="Supervisor" or puesto=="Coordinador":      

    placeholder10_7 = st.empty()
    personal_7 = placeholder10_7.selectbox("Personal", options=("Todos","Operarios","Propio","Personal Asignado"), key="filtro_7")

    placeholder11_7 = st.empty()
    proceso_7_s = placeholder11_7.selectbox("Proceso", options=("Todos","Conformación","Control de Calidad Conformación","Información Final I","Control de Calidad IF I","Información Final II","Información Final III"), key="proceso_7_s")
    
    placeholder12_7 = st.empty()
    tipo_7_s = placeholder12_7.selectbox("Tipo", options=("Todos","Ordinario","Corrección Primera Revisión","Corrección Segunda Revisión","Corrección Tercera o Más Revisiones"), key="tipo_7_s")

    if personal_7=="Todos" and proceso_7_s=="Todos" and tipo_7_s=="Todos":
        
        data_1=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
        data_2 = data_1.groupby(["nombre", "fecha"], as_index=False)["predios","horas"].agg(np.sum)
        data_3 = data_1.groupby(["fecha"], as_index=False)["predios"].agg(np.sum)

    elif personal_7=="Todos" and proceso_7_s=="Todos" and tipo_7_s!="Todos":
        
        data_1=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where tipo='{tipo_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
        data_2 = data_1.groupby(["nombre", "fecha"], as_index=False)["predios","horas"].agg(np.sum)
        data_3 = data_1.groupby(["fecha"], as_index=False)["predios"].agg(np.sum)

    elif personal_7=="Todos" and proceso_7_s !="Todos" and tipo_7_s=="Todos":
        
        data_1=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where proceso='{proceso_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
        data_2 = data_1.groupby(["nombre", "fecha"], as_index=False)["predios","horas"].agg(np.sum)
        data_3 = data_1.groupby(["fecha"], as_index=False)["predios"].agg(np.sum)

    elif personal_7=="Todos" and proceso_7_s !="Todos" and tipo_7_s!="Todos":
        
        data_1=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where proceso='{proceso_7_s}' and tipo='{tipo_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
        data_2 = data_1.groupby(["nombre", "fecha"], as_index=False)["predios","horas"].agg(np.sum)
        data_3 = data_1.groupby(["fecha"], as_index=False)["predios"].agg(np.sum)


    elif personal_7=="Operarios" and proceso_7_s =="Todos" and tipo_7_s=="Todos":
       
        data_1=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where puesto='Operario Catastral' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
        data_2 = data_1.groupby(["nombre", "fecha"], as_index=False)["predios","horas"].agg(np.sum)
        data_3 = data_1.groupby(["fecha"], as_index=False)["predios"].agg(np.sum)

    elif personal_7=="Operarios" and proceso_7_s =="Todos" and tipo_7_s!="Todos":
       
        data_1=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where puesto='Operario Catastral' and tipo='{tipo_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
        data_2 = data_1.groupby(["nombre", "fecha"], as_index=False)["predios","horas"].agg(np.sum)
        data_3 = data_1.groupby(["fecha"], as_index=False)["predios"].agg(np.sum)

    elif personal_7=="Operarios" and proceso_7_s !="Todos" and tipo_7_s=="Todos":
        
        data_1=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where puesto='Operario Catastral' and proceso='{proceso_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
        data_2 = data_1.groupby(["nombre", "fecha"], as_index=False)["predios","horas"].agg(np.sum)
        data_3 = data_1.groupby(["fecha"], as_index=False)["predios"].agg(np.sum)

    elif personal_7=="Operarios" and proceso_7_s !="Todos" and tipo_7_s!="Todos":
        
        data_1=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where puesto='Operario Catastral' and tipo='{tipo_7_s}' and proceso='{proceso_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
        data_2 = data_1.groupby(["nombre", "fecha"], as_index=False)["predios","horas"].agg(np.sum)
        data_3 = data_1.groupby(["fecha"], as_index=False)["predios"].agg(np.sum)

    elif personal_7=="Propio" and proceso_7_s=="Todos" and tipo_7_s=="Todos":
        
        data_1=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where usuario='{usuario}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
        data_2 = data_1.groupby(["nombre", "fecha"], as_index=False)["predios","horas"].agg(np.sum)
        data_3 = data_1.groupby(["fecha"], as_index=False)["predios"].agg(np.sum)

    elif personal_7=="Propio" and proceso_7_s=="Todos" and tipo_7_s!="Todos":
        
        data_1=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where usuario='{usuario}' and tipo='{tipo_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
        data_2 = data_1.groupby(["nombre", "fecha"], as_index=False)["predios","horas"].agg(np.sum)
        data_3 = data_1.groupby(["fecha"], as_index=False)["predios"].agg(np.sum)

    elif personal_7=="Propio" and proceso_7_s !="Todos" and tipo_7_s=="Todos":
        
        data_1=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where usuario='{usuario}' and proceso='{proceso_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
        data_2 = data_1.groupby(["nombre", "fecha"], as_index=False)["predios","horas"].agg(np.sum)
        data_3 = data_1.groupby(["fecha"], as_index=False)["predios"].agg(np.sum)

    elif personal_7=="Propio" and proceso_7_s !="Todos" and tipo_7_s!="Todos":
        
        data_1=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where usuario='{usuario}' and tipo='{tipo_7_s}' and proceso='{proceso_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
        data_2 = data_1.groupby(["nombre", "fecha"], as_index=False)["predios","horas"].agg(np.sum)
        data_3 = data_1.groupby(["fecha"], as_index=False)["predios"].agg(np.sum)

    elif personal_7=="Personal Asignado" and proceso_7_s =="Todos" and tipo_7_s=="Todos":
        
        data_1=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where supervisor='{nombre_7}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
        data_2 = data_1.groupby(["nombre", "fecha"], as_index=False)["predios","horas"].agg(np.sum)
        data_3 = data_1.groupby(["fecha"], as_index=False)["predios"].agg(np.sum)
    
    elif personal_7=="Personal Asignado" and proceso_7_s =="Todos" and tipo_7_s!="Todos":
        
        data_1=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where supervisor='{nombre_7}' and tipo='{tipo_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
        data_2 = data_1.groupby(["nombre", "fecha"], as_index=False)["predios","horas"].agg(np.sum)
        data_3 = data_1.groupby(["fecha"], as_index=False)["predios"].agg(np.sum)

    elif personal_7=="Personal Asignado" and proceso_7_s !="Todos" and tipo_7_s=="Todos":
       
        data_1=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where supervisor='{nombre_7}' and proceso='{proceso_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
        data_2 = data_1.groupby(["nombre", "fecha"], as_index=False)["predios","horas"].agg(np.sum)
        data_3 = data_1.groupby(["fecha"], as_index=False)["predios"].agg(np.sum)
    
    elif personal_7=="Personal Asignado" and proceso_7_s !="Todos" and tipo_7_s!="Todos":
       
        data_1=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where supervisor='{nombre_7}' and tipo='{tipo_7_s}' and proceso='{proceso_7_s}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
        data_2 = data_1.groupby(["nombre", "fecha"], as_index=False)["predios","horas"].agg(np.sum)
        data_3 = data_1.groupby(["fecha"], as_index=False)["predios"].agg(np.sum)

  # ----- Datos Operario Catastral ---- #

  elif puesto=="Operario Catastral":

    placeholder13_7 = st.empty()
    proceso_7_o= placeholder13_7.selectbox("Proceso", options=("Todos","Conformación","Control de Calidad Conformación","Información Final I","Control de Calidad IF I","Información Final II","Información Final III"), key="proceso_7_o")

    placeholder14_7 = st.empty()
    tipo_7_o = placeholder14_7.selectbox("Tipo", options=("Todos","Ordinario","Corrección Primera Revisión","Corrección Segunda Revisión","Corrección Tercera o Más Revisiones"), key="tipo_7_o")    

    if proceso_7_o =="Todos" and tipo_7_o=="Todos":
        
      data_1=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where usuario='{usuario}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2 = data_1.groupby(["nombre", "fecha"], as_index=False)["predios","horas"].agg(np.sum)
    
    elif proceso_7_o =="Todos" and tipo_7_o!="Todos":
        
      data_1=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where usuario='{usuario}' and tipo='{tipo_7_o}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2 = data_1.groupby(["nombre", "fecha"], as_index=False)["predios","horas"].agg(np.sum)

    elif proceso_7_o !="Todos" and tipo_7_o=="Todos":
        
      data_1=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where usuario='{usuario}' and proceso='{proceso_7_o}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2 = data_1.groupby(["nombre", "fecha"], as_index=False)["predios","horas"].agg(np.sum)

    elif proceso_7_o !="Todos" and tipo_7_o!="Todos":
        
      data_1=pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,horario,puesto,supervisor,proceso,fecha,bloque,estado,tipo,cast(predios as integer),cast(horas as float) from registro where usuario='{usuario}' and proceso='{proceso_7_o}' and tipo='{tipo_7_o}' and fecha>='{fecha_de__inicio_7}' and fecha<='{fecha_de__finalizacion_7}'", con)
      data_2 = data_1.groupby(["nombre", "fecha"], as_index=False)["predios","horas"].agg(np.sum)

  # ----- Reportes ---- #
  
  placeholder15_7 = st.empty()
  reportes_7=placeholder15_7.subheader("Reportes")   

  placeholder16_7 = st.empty()
  historial_7_data_1=placeholder16_7.dataframe(data=data_1)

  placeholder17_7 = st.empty()
  descarga_7_data_1 = placeholder17_7.download_button("Decargar CSV",data=data_1.to_csv(),mime="text/csv",key="descarga_7_data_1")

  # ----- Resumen ---- #

  placeholder18_7 = st.empty()
  resumen_7=placeholder18_7.subheader("Resumen")  

  placeholder19_7 = st.empty()
  historial_7_data_2= placeholder19_7.dataframe(data=data_2)

  placeholder20_7 = st.empty()
  descarga_7_data_2 = placeholder20_7.download_button("Decargar CSV",data=data_2.to_csv(),mime="text/csv",key="descarga_7_data_2")

  nombre_7_2=data_2.iloc[:,0]
  pivot=len(nombre_7_2)

  if pivot==0:

    placeholder21_7 = st.empty()
    error= placeholder21_7.error('No existen datos para mostrar')

  else:
    
    fecha_7_2=data_2.iloc[:,1]
    predio_7_2=data_2.iloc[:,2]
    d = {'col1':nombre_7_2, 'col2':fecha_7_2,'col3':predio_7_2 }
    df = pd.DataFrame(data=d)
    lista_nombres_7_2 = df["col1"].unique().tolist()

    placeholder22_7 = st.empty()
    nombres= placeholder22_7.multiselect("Seleccionar",lista_nombres_7_2)

    dfs = {nombre: df[df["col1"] == nombre] for nombre in nombres}
    fig_2 = go.Figure()
    for nombre, df in dfs.items():
      fig_2 = fig_2.add_trace(go.Scatter(x=df["col2"], y=df["col3"], name=nombre))

    placeholder23_7 = st.empty()
    grafico_7_2= placeholder23_7.plotly_chart(fig_2)

    # ----- Total ---- #

    if puesto=="Supervisor" or puesto=="Coordinador":

      placeholder24_7 = st.empty()
      total_7=placeholder24_7.subheader("Total")  
        
      fig_3 = px.bar(data_3, x="fecha", y="predios", text="predios")
      fig_3.update_traces(textposition="outside")
      placeholder25_7 = st.empty()
      grafico_7_3= placeholder25_7.plotly_chart(fig_3)

      placeholder26_7 = st.empty()
      descarga_7_data_3 = placeholder26_7.download_button("Decargar CSV",data=data_3.to_csv(),mime="text/csv",key="descarga_7_data_3")

  # ----- Procesos ---- #
    
  if procesos_7:
    placeholder1_7.empty()
    placeholder2_7.empty()
    placeholder3_7.empty()
    placeholder4_7.empty()
    placeholder5_7.empty()   
    placeholder6_7.empty()
    placeholder7_7.empty()
    placeholder8_7.empty()
    placeholder9_7.empty()
    if puesto=="Supervisor" or puesto=="Coordinador":  
      placeholder10_7.empty()
      placeholder11_7.empty()
      placeholder12_7.empty()
    elif puesto=="Operario Catastral": 
      placeholder13_7.empty()
      placeholder14_7.empty()
    placeholder15_7.empty()
    placeholder16_7.empty()
    placeholder17_7.empty()
    placeholder18_7.empty()
    placeholder19_7.empty()
    placeholder20_7.empty()
    if pivot!=0 and puesto=="Operario Catastral": 
      placeholder22_7.empty()
      placeholder23_7.empty()
    elif pivot!=0 and puesto=="Supervisor":
      placeholder22_7.empty()
      placeholder23_7.empty()
      placeholder24_7.empty()
      placeholder25_7.empty()
      placeholder26_7.empty()
    elif pivot!=0 and puesto=="Coordinador":
      placeholder22_7.empty()
      placeholder23_7.empty()
      placeholder24_7.empty()
      placeholder25_7.empty()
      placeholder26_7.empty()
    if pivot==0:
      placeholder21_7.empty()
    st.session_state.Procesos=False
    st.session_state.Historial=False

    perfil=pd.read_sql(f"select perfil from usuarios where usuario ='{usuario}'",uri)
    perfil= perfil.loc[0,'perfil']

    if perfil=="1":        
                    
      Procesos.Procesos1(usuario,puesto)
                
    elif perfil=="2":        
                    
      Procesos.Procesos2(usuario,puesto)   

    elif perfil=="3":  

      Procesos.Procesos3(usuario,puesto)       

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
    placeholder9_7.empty()
    if puesto=="Supervisor" or puesto=="Coordinador":  
      placeholder10_7.empty()
      placeholder11_7.empty()
      placeholder12_7.empty()
    elif puesto=="Operario Catastral": 
      placeholder13_7.empty()
      placeholder14_7.empty()
    placeholder15_7.empty()
    placeholder16_7.empty()
    placeholder17_7.empty()
    placeholder18_7.empty()
    placeholder19_7.empty()
    placeholder20_7.empty()
    if pivot!=0 and puesto=="Operario Catastral": 
      placeholder22_7.empty()
      placeholder23_7.empty()
    elif pivot!=0 and puesto=="Supervisor":
      placeholder22_7.empty()
      placeholder23_7.empty()
      placeholder24_7.empty()
      placeholder25_7.empty()
      placeholder26_7.empty()
    elif pivot!=0 and puesto=="Coordinador":
      placeholder22_7.empty()
      placeholder23_7.empty()
      placeholder24_7.empty()
      placeholder25_7.empty()
      placeholder26_7.empty()
    if pivot==0:
      placeholder21_7.empty()
    st.session_state.Historial=False
    st.session_state.Capacitacion=True
    Capacitacion.Capacitacion(usuario,puesto)

  # ----- Otros Registros ---- #
    
  elif otros_registros_7:
    placeholder1_7.empty()
    placeholder2_7.empty()
    placeholder3_7.empty()
    placeholder4_7.empty()
    placeholder5_7.empty()   
    placeholder6_7.empty()
    placeholder7_7.empty()
    placeholder8_7.empty()
    placeholder9_7.empty()
    if puesto=="Supervisor" or puesto=="Coordinador":  
      placeholder10_7.empty()
      placeholder11_7.empty()
      placeholder12_7.empty()
    elif puesto=="Operario Catastral": 
      placeholder13_7.empty()
      placeholder14_7.empty()
    placeholder15_7.empty()
    placeholder16_7.empty()
    placeholder17_7.empty()
    placeholder18_7.empty()
    placeholder19_7.empty()
    placeholder20_7.empty()
    if pivot!=0 and puesto=="Operario Catastral": 
      placeholder22_7.empty()
      placeholder23_7.empty()
    elif pivot!=0 and puesto=="Supervisor":
      placeholder22_7.empty()
      placeholder23_7.empty()
      placeholder24_7.empty()
      placeholder25_7.empty()
      placeholder26_7.empty()
    elif pivot!=0 and puesto=="Coordinador":
      placeholder22_7.empty()
      placeholder23_7.empty()
      placeholder24_7.empty()
      placeholder25_7.empty()
      placeholder26_7.empty()
    if pivot==0:
      placeholder21_7.empty()
    st.session_state.Historial=False
    st.session_state.Otros_Registros=True
    Otros_Registros.Otros_Registros(usuario,puesto)

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
    placeholder9_7.empty()
    if puesto=="Supervisor" or puesto=="Coordinador":  
      placeholder10_7.empty()
      placeholder11_7.empty()
      placeholder12_7.empty()
    elif puesto=="Operario Catastral": 
      placeholder13_7.empty()
      placeholder14_7.empty()
    placeholder15_7.empty()
    placeholder16_7.empty()
    placeholder17_7.empty()
    placeholder18_7.empty()
    placeholder19_7.empty()
    placeholder20_7.empty()
    if pivot!=0 and puesto=="Operario Catastral": 
      placeholder22_7.empty()
      placeholder23_7.empty()
    elif pivot!=0 and puesto=="Supervisor":
      placeholder22_7.empty()
      placeholder23_7.empty()
      placeholder24_7.empty()
      placeholder25_7.empty()
      placeholder26_7.empty()
    elif pivot!=0 and puesto=="Coordinador":
      placeholder22_7.empty()
      placeholder23_7.empty()
      placeholder24_7.empty()
      placeholder25_7.empty()
      placeholder26_7.empty()
    if pivot==0:
      placeholder21_7.empty()
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
    placeholder9_7.empty()
    if puesto=="Supervisor" or puesto=="Coordinador":  
      placeholder10_7.empty()
      placeholder11_7.empty()
      placeholder12_7.empty()
    elif puesto=="Operario Catastral": 
      placeholder13_7.empty()
      placeholder14_7.empty()
    placeholder15_7.empty()
    placeholder16_7.empty()
    placeholder17_7.empty()
    placeholder18_7.empty()
    placeholder19_7.empty()
    placeholder20_7.empty()
    if pivot!=0 and puesto=="Operario Catastral": 
      placeholder22_7.empty()
      placeholder23_7.empty()
    elif pivot!=0 and puesto=="Supervisor":
      placeholder22_7.empty()
      placeholder23_7.empty()
      placeholder24_7.empty()
      placeholder25_7.empty()
      placeholder26_7.empty()
    elif pivot!=0 and puesto=="Coordinador":
      placeholder22_7.empty()
      placeholder23_7.empty()
      placeholder24_7.empty()
      placeholder25_7.empty()
      placeholder26_7.empty()
    if pivot==0:
      placeholder21_7.empty()
    st.session_state.Ingreso = False
    st.session_state.Historial=False
    st.session_state.Salir=True
    Salir.Salir()