# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest17406(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    pending = list(str(referer_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
