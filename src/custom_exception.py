'''
Este archivo define una excepción personalizada (CustomException) que, cuando ocurre un error, 
construye un mensaje claro con el archivo y la línea exacta donde falló, más el mensaje original. 
Así, cualquier persona puede identificar rápido el origen del problema sin leer trazas largas. 
Se usa junto con logger.py para que estos mensajes queden guardados automáticamente en el log del proyecto.

Ejemplo de mensaje en el log:
2025-11-10 10:15:32,847 - ERROR - Error occurred in script: d:\IMPA\MLOps\1_Hotel\src\mi_modulo.py at line: 42 with message: division by zero
'''


import traceback
import sys

# CustomException(Exception) hereda de Exception
class CustomException(Exception):

    def __init__(self, error_message, error_detail:sys):    # (init): se ejecuta al crear el objeto
        super().__init__(error_message)                     # Es la forma de llamar a la implementación de la clase padre desde una clase hija.
        self.error_message = self.get_detailed_error_message(error_message, error_detail)

    # No usa self ni datos de clase; solo parámetros. Por eso no depende de estado.
    @staticmethod
    def get_detailed_error_message(error_message, error_detail:sys):
        _ , _ , exc_tb = traceback.sys.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno

        return f"Error occurred in script: {file_name} at line: {line_number} with message: {error_message}"
    
    def __str__(self):
        return self.error_message
    