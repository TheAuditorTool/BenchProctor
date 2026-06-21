# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import json


def BenchmarkTest01304(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = json.loads(json_value).get('value', '')
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return JsonResponse({"saved": True})
