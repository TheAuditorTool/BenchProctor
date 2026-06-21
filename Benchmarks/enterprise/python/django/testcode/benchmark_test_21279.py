# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest21279(request):
    raw_body = request.body.decode('utf-8')
    data, _sep, _rest = str(raw_body).partition('\x00')
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
