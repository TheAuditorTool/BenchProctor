# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import base64


def BenchmarkTest34074(request):
    raw_body = request.body.decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return JsonResponse({"saved": True})
