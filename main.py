#API: aplication programing interface
#mas que algo como tal es un concepto
#es la manera en que dos aplicaciones se van a cenectar 
#hay diferentes tipos de api, aprenderemos api rest
#para construir un aapi existen varias librerias 
#django, flask, y actualmente una muy popular es fastAPI

from fastapi import FastAPI


app = FastAPI()  
#instancia de la clase FatsAPI
#decorador es una funcion que recibe como argumento una fucion y deuelve otra funcion se utiliza un @

@app.get("/")
def root():
    return {
        "respuesta": "Hola mundo "
    }


#el que se actualice se llama hob reload y se produce porque en el codigo yo le doy --reload
#aplicando 127.0.0.1:8000 en google aparece mi mensaje
#la api tenen la dcumentacion y hay de dos tipos
#127.0.0.1:8000/docs 
#127.0.0.1:8000/redoc con esto lo que puede hacer es compartir la api,

@app.get("/home")
def root():
    return {
        "respuesta": "Hola en el home "
    }
