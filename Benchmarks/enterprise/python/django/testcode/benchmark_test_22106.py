# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import shlex


def to_text(value):
    return str(value).strip()

def BenchmarkTest22106(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = to_text(auth_header)
    processed = shlex.quote(data)
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
