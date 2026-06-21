# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import os


def BenchmarkTest56672(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
