# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest63940(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = referer_value if referer_value else 'default'
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
