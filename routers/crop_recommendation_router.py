from fastapi import APIRouter
from schemas.crop_recommendation_schemas import CropRecommendationData
from services.crop_recommendation_service import predict_crop_rf, predict_crop_svm

router = APIRouter()

@router.post('/predict_rf')
async def crop_predict_rf(data: CropRecommendationData):
    prediction = predict_crop_rf(data)
    return {"model": "RandomForest", "recommendation": prediction}

@router.post('/predict_svm')
async def crop_predict_svm(data: CropRecommendationData):
    prediction = predict_crop_svm(data)
    return {"model": "SVM", "recommendation": prediction}