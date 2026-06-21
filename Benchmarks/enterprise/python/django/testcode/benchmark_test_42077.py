# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import shlex


def BenchmarkTest42077(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = str(header_value).replace('\x00', '')
    processed = shlex.quote(data)
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
