# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest31607(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = str(host_value).replace('\x00', '')
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
