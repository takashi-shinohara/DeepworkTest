from pickle import FALSE, TRUE
from django.shortcuts import render
import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import random

@ensure_csrf_cookie
def dummyAI(request):
    datas = json.loads(request.body)
    imagePath = datas.get("image_path")

    # 仮の返却データ
    successData = {
        "success": "true",
        "message": "success",
        "estimated_data": {"class": 3, "confidence": 0.8683}
    }
    errorData = {
        "success": "false",
        "message": "Error:E50012",
        "estimated_data": {}
    }

    if len(imagePath) == 0 :
        reslut = errorData
    else:
        reslut = successData

    # JSONに変換して戻す
    return JsonResponse(reslut)
