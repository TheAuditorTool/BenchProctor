# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import json
import os


def BenchmarkTest22921(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
