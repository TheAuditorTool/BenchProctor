# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def relay_value(value):
    return value

def BenchmarkTest74002(request):
    upload_name = request.FILES['upload'].name
    data = relay_value(upload_name)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
