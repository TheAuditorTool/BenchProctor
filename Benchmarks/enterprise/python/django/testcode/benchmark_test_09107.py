# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import json


def BenchmarkTest09107(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = str(json_value).replace('\x00', '')
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
