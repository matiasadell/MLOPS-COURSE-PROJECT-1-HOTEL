# 🏨 Hotel Booking Cancellation Prediction

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![GCP](https://img.shields.io/badge/GCP-Cloud%20Run-red.svg)](https://cloud.google.com/)
[![MLflow](https://img.shields.io/badge/MLflow-Tracking-orange.svg)](https://mlflow.org/)
[![Jenkins](https://img.shields.io/badge/Jenkins-CI/CD-red.svg)](https://www.jenkins.io/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-blue.svg)](https://www.docker.com/)


Sistema end-to-end de Machine Learning que predice cancelaciones de reservas hoteleras con pipeline automatizado de CI/CD y deployment en producción.

## Descripción del Proyecto

Este proyecto implementa un sistema completo de MLOps que automatiza desde la ingesta de datos hasta el deployment de un modelo en producción. El modelo predice si una reserva hotelera será cancelada, permitiendo a los hoteles optimizar su gestión de inventario y estrategias de pricing.

**Problema de negocio:** Las cancelaciones de reservas generan pérdidas económicas significativas. Un sistema predictivo permite tomar acciones preventivas (overbooking controlado, políticas de cancelación dinámicas, ofertas personalizadas).

## Dataset

El proyecto utiliza el [Hotel Reservations Classification Dataset](https://www.kaggle.com/datasets/ahsan81/hotel-reservations-classification-dataset) de Kaggle, que contiene 36,275 reservas hoteleras con 19 características incluyendo:

- **Características temporales:** lead_time, arrival_date, arrival_month
- **Información de la reserva:** no_of_adults, no_of_children, required_car_parking_space
- **Datos del cliente:** type_of_meal_plan, room_type_reserved, market_segment_type
- **Historial de reservas:** no_of_previous_cancellations, no_of_previous_bookings_not_canceled
- **Target:** booking_status (Cancelado/No Cancelado)

## Arquitectura

<img width="1104" height="691" alt="image" src="https://github.com/user-attachments/assets/187af0c2-8870-402e-9146-0962eebd6c95" />

## Pipeline de Machine Learning

El pipeline de datos comienza con la ingesta automática desde Google Cloud Storage, donde se descarga el dataset de reservas hoteleras y se divide en conjuntos de entrenamiento y test con una proporción 80/20. Posteriormente, en la etapa de feature engineering, se aplican múltiples transformaciones: primero se realiza label encoding para convertir variables categóricas como tipo de habitación y segmento de mercado en valores numéricos, luego se maneja la asimetría (skewness) de las variables numéricas mediante transformaciones logarítmicas, se balancea el dataset usando SMOTE para compensar el desbalance entre reservas canceladas y confirmadas, y finalmente se seleccionan las 10 features más importantes utilizando Random Forest basándose en feature importance.

El pipeline de modelado utiliza LightGBM Classifier como algoritmo de clasificación. La optimización de hiperparámetros se realiza mediante RandomizedSearchCV, que explora diferentes combinaciones de parámetros para encontrar la configuración óptima del modelo. Todo el proceso de experimentación se registra en MLflow, que permite el tracking de parámetros, métricas y versiones del modelo. Las métricas evaluadas incluyen Accuracy, Precision, Recall y F1-Score para medir el rendimiento del clasificador.

## API de Predicciones

El modelo entrenado se despliega como una API REST mediante Flask, permitiendo realizar predicciones en tiempo real. La aplicación Flask recibe requests HTTP con los datos de la reserva y devuelve la probabilidad de cancelación. Esta API queda containerizada en Docker y desplegada en Google Cloud Run, garantizando escalabilidad automática y alta disponibilidad para servir predicciones a sistemas de reservas en producción.



## CI/CD y Deployment

El flujo de integración y despliegue continuo dispara automáticamente el pipeline de Jenkins. Jenkins clona el repositorio, crea un entorno virtual de Python, instala las dependencias necesarias y construye una imagen Docker con toda la aplicación. Esta imagen se empaqueta con el modelo entrenado y la API Flask para servir predicciones. Una vez construida, la imagen se sube a Google Container Registry (GCR) donde queda almacenada y versionada. Finalmente, Jenkins ejecuta el comando de deployment que despliega automáticamente la imagen en Google Cloud Run, donde la API queda disponible para recibir requests y devolver predicciones en tiempo real sin necesidad de intervención manual.

