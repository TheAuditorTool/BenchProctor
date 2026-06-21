# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json
import subprocess


def BenchmarkTest01877(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = '{}'.format(json_value)
    subprocess.run([str(data), '--status'], shell=False)
    return JsonResponse({"saved": True})
