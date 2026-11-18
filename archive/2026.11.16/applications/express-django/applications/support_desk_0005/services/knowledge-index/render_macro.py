# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import base64
import requests
from app_runtime import redis_client


@csrf_exempt
def render_macro(request):
    phrase = redis_client.get('user_data')
    inquiry = base64.b64decode(phrase).decode('utf-8', 'ignore')
    requests.get(str(inquiry))
    return JsonResponse({"saved": True})
