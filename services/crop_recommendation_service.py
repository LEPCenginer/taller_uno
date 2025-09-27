import pickle
import numpy as np
from schemas.crop_recommendation_schemas import CropRecommendationData

# Cargar modelos
with open('RFCROP_recommendation.pkl', 'rb') as f:
    rf_model = pickle.load(f)
try:
    with open('SVMCROP_recommendation.pkl', 'rb') as f:
        svm_model = pickle.load(f)
except FileNotFoundError:
    svm_model = None

# Etiquetas de cultivos (ajustar según el dataset)
crop_labels = [
    'rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas', 'mothbeans',
    'mungbean', 'blackgram', 'lentil', 'pomegranate', 'banana', 'mango',
    'grapes', 'watermelon', 'muskmelon', 'apple', 'orange', 'papaya',
    'coconut', 'cotton', 'jute', 'coffee'
]

def predict_crop_rf(data: CropRecommendationData):
    xin = np.array([
        data.N, data.P, data.K, data.temperature, data.humidity, data.ph, data.rainfall
    ]).reshape(1, -1)
    pred = rf_model.predict(xin)
    return pred[0]

def predict_crop_svm(data: CropRecommendationData):
    if svm_model is None:
        return 'SVM model not available'
    xin = np.array([
        data.N, data.P, data.K, data.temperature, data.humidity, data.ph, data.rainfall
    ]).reshape(1, -1)
    pred = svm_model.predict(xin)
    return pred[0]
