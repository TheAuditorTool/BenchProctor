# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import json


def BenchmarkTest17253(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = ' '.join(str(json_value).split())
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return JsonResponse({"saved": True})
