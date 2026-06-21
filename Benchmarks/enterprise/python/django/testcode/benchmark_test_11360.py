# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os


request_state: dict[str, str] = {}

def BenchmarkTest11360(request):
    user_id = request.GET.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        requests.get(str(data))
    return JsonResponse({"saved": True})
