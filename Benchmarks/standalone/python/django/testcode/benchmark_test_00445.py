# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import os


def BenchmarkTest00445(request):
    env_value = os.environ.get('APP_INPUT', '')
    data = str(env_value).replace('\x00', '')
    parsed = yaml.safe_load(data)
    return JsonResponse({'parsed': str(parsed)}, status=200)
