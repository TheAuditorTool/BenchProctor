# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest02503(request):
    raw_body = request.body.decode('utf-8')
    requests.post('https://api.prod.internal/data', data=str(raw_body), verify=True)
    return JsonResponse({"saved": True})
