# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import json


def BenchmarkTest55286(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
