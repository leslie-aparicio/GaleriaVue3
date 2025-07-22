from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import pymysql

app = FastAPI()

# Permitir solicitudes CORS desde tu frontend (ajustar según el caso)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solicitudes desde cualquier origen
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados
)

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

def get_db_connection():
    return pymysql.connect(
        host="localhost",
        user="root",  
        password="1234",  
        database="galeria",
        cursorclass=pymysql.cursors.DictCursor
    )

@app.get("/images")
def get_images():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM imagenes")
    images = cursor.fetchall()
    conn.close()
    return images
