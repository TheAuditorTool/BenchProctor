# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest14118(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = f'{referer_value}'
    requests.get(str(data))
    return JsonResponse({"saved": True})
