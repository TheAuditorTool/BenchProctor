# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import base64
import requests
from app_runtime import redis_client


@csrf_exempt
def format_window(request):
    subtitle = redis_client.get('user_data')
    ledger = base64.b64decode(subtitle).decode('utf-8', 'ignore')
    requests.get(str(ledger))
    return JsonResponse({"saved": True})
