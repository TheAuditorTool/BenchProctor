# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest71917(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = f'{referer_value:.200s}'
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
