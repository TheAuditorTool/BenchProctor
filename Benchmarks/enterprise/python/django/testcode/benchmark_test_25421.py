# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest25421(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = str(referer_value).replace('\x00', '')
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
