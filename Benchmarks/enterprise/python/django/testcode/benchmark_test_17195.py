# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import json
import os


def BenchmarkTest17195(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = str(env_value).replace('\x00', '')
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
