# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def to_text(value):
    return str(value).strip()

def BenchmarkTest73964(request):
    upload_name = request.FILES['upload'].name
    data = to_text(upload_name)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
