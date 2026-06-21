# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest02013(request):
    upload_name = request.FILES['upload'].name
    data, _sep, _rest = str(upload_name).partition('\x00')
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
