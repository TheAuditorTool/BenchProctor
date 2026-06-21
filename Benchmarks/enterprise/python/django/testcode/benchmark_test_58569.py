# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest58569(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    requests.post('http://api.prod.internal/data', data=str(origin_value))
    return JsonResponse({"saved": True})
