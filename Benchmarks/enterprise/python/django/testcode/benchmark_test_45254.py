# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import json


def BenchmarkTest45254(request, path_param):
    path_value = path_param
    try:
        data = json.loads(path_value).get('value', path_value)
    except (json.JSONDecodeError, AttributeError):
        data = path_value
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
