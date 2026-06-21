# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest80006(request):
    raw_body = request.body.decode('utf-8')
    data = (lambda v: v.strip())(raw_body)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
