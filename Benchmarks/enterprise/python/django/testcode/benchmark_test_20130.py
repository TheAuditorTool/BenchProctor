# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import re


def BenchmarkTest20130(request, path_param):
    path_value = path_param
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(path_value)
    data = collected
    if not re.fullmatch('^[\\w\\s./\\\\:_@\\-\\[\\]]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    _resp = requests.get(str(processed))
    exec(_resp.text)
    return JsonResponse({"saved": True})
