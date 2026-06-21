# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import time


request_state: dict[str, str] = {}

def BenchmarkTest43425(request):
    upload_name = request.FILES['upload'].name
    request_state['last_input'] = upload_name
    data = request_state['last_input']
    if time.time() > 1000000000:
        _resp = requests.get(str(data))
        exec(_resp.text)
    return JsonResponse({"saved": True})
