# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
import json


def BenchmarkTest71757(request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
