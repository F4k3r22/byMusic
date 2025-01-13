from dataclasses import dataclass
from flask import Flask, request, jsonify, render_template
import MySQLdb
from TubeKit import YouTubeClient


@dataclass
class MySQLConfig:
    """ MySQL Configuration """
    host: str = "localhost"
    user: str = "root"
    password: str = "root"
    database: str = "music"

config = MySQLConfig()

def testconnetion():
    try:
        print(f"Probando conexión a MySQL con {config}")
        connection = MySQLdb.connect(
            host=config.host,
            user=config.user,
            password=config.password,
            database=config.database
        )
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        print(f"Conexión exitosa" if result else "Error en la consulta")

        return "Conexión exitosa" if result else "Error en la consulta"

    except Exception as e:
        return f"Error de conexión: {str(e)}"

        
testconnetion()