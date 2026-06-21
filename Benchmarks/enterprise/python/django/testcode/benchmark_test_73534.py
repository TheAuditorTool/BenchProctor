# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def relay_value(value):
    return value

def BenchmarkTest73534(request):
    upload_name = request.FILES['upload'].name
    data = relay_value(upload_name)
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
