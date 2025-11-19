"""Proporciona un único punto para guardar los logs que genera la aplicación.
Sirve para revisar qué ocurrió cuando algo falla y seguir la actividad del proyecto, útil para mantenimiento y diagnóstico por el equipo.
"""

import logging
import os
from datetime import datetime

# Crear carpeta logs
LOGS_DIR = "logs"
os.makedirs(LOGS_DIR, exist_ok=True) # Crear solo si no existe

# Example: log_2025-02-21.log
LOG_FILE = os.path.join(LOGS_DIR, f"log_{datetime.now().strftime('%Y%m%d')}.log")

# Tres niveles de logging: DEBUG, INFO, ERROR
logging.basicConfig(
    filename=LOG_FILE,
    format='%(asctime)s - %(levelname)s - %(message)s', # 2025-02-21 - INFO - "Hello world"
    level=logging.INFO # Solo registrar mensajes de nivel INFO o mensajes de error
)

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger