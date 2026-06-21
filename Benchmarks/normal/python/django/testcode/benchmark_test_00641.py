# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import urllib.request


def BenchmarkTest00641(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
