# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import time


def relay_value(value):
    return value

def BenchmarkTest02956(request):
    upload_name = request.FILES['upload'].name
    data = relay_value(upload_name)
    if time.time() > 1000000000:
        requests.get(str(data))
    return JsonResponse({"saved": True})
