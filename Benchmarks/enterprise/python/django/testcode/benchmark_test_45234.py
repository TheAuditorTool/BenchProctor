# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import os


def BenchmarkTest45234(request):
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
