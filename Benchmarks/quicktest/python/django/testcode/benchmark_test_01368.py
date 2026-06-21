# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import os


def BenchmarkTest01368(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
