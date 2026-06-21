# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os


def BenchmarkTest45867(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = str(env_value).replace('\x00', '')
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
