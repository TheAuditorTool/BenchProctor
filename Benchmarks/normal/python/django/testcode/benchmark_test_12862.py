# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest12862(request):
    raw_body = request.body.decode('utf-8')
    requests.post('http://api.prod.internal/data', data=str(raw_body))
    return JsonResponse({"saved": True})
