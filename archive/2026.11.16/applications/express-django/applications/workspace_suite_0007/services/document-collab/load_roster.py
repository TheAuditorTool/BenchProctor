# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import base64
import requests
from app_runtime import redis_client


@csrf_exempt
def load_roster(request):
    summary = redis_client.get('user_data')
    subtitle = base64.b64decode(summary).decode('utf-8', 'ignore')
    requests.get(str(subtitle))
    return JsonResponse({"saved": True})
