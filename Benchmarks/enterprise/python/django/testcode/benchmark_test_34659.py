# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import json


def BenchmarkTest34659(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = f'{json_value}'
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
