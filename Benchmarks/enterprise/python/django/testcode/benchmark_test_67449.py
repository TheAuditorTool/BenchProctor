# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest67449(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '{}'.format(host_value)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
