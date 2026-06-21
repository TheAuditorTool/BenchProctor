# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os


def BenchmarkTest48813(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    requests.get(str(data))
    return JsonResponse({"saved": True})
