# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest65979(request):
    raw_body = request.body.decode('utf-8')
    _resp = requests.get(str(raw_body))
    exec(_resp.text)
    return JsonResponse({"saved": True})
