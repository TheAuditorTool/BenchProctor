# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json
import subprocess


def BenchmarkTest16944(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    try:
        data = json.loads(referer_value).get('value', referer_value)
    except (json.JSONDecodeError, AttributeError):
        data = referer_value
    subprocess.run([str(data), '--status'], shell=False)
    return JsonResponse({"saved": True})
