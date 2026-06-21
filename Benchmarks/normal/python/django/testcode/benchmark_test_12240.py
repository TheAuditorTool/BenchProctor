# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest12240(request):
    raw_body = request.body.decode('utf-8')
    data = str(raw_body).replace('\x00', '')
    requests.get(str(data))
    return JsonResponse({"saved": True})
