# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest29088(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    pending = list(str(ua_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
