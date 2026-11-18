# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import os


def BenchmarkTest00260(request):
    env_value = os.environ.get('APP_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
