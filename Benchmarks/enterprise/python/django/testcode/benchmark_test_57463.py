# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest57463(request):
    raw_body = request.body.decode('utf-8')
    requests.get(str(raw_body))
    return JsonResponse({"saved": True})
