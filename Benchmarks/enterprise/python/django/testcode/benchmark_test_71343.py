# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest71343(request):
    raw_body = request.body.decode('utf-8')
    if raw_body:
        data = raw_body
    else:
        data = ''
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
