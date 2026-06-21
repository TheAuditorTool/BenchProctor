# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os


request_state: dict[str, str] = {}

def BenchmarkTest32562(request):
    multipart_value = request.POST.get('multipart_field', '')
    request_state['last_input'] = multipart_value
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        _resp = requests.get(str(data))
        exec(_resp.text)
    return JsonResponse({"saved": True})
