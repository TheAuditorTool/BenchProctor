# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def relay_value(value):
    return value

def BenchmarkTest59818(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = relay_value(multipart_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
