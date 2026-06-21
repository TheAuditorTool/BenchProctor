# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
import json


def BenchmarkTest61612(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    parts = str(json_value).split(',')
    data = ','.join(parts)
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
