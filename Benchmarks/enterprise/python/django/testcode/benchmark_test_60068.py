# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest60068(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    prefix = ''
    data = prefix + str(origin_value)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
