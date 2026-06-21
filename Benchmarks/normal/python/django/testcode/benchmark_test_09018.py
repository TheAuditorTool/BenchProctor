# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import os


def BenchmarkTest09018(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
