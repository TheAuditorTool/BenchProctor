# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import base64


def BenchmarkTest42122(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
