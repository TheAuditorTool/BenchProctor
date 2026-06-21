# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import re
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest44876(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = to_text(env_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
