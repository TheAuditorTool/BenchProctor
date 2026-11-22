# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import json


def BenchmarkTest00143(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    data = (lambda v: v.strip())(json_value)
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return JsonResponse({"saved": True})
