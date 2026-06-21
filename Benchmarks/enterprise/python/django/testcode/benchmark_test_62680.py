# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import re


def relay_value(value):
    return value

def BenchmarkTest62680(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = relay_value(referer_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
