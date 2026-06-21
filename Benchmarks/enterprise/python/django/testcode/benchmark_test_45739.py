# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import json


def coalesce_blank(value):
    return value or ''

def BenchmarkTest45739(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = coalesce_blank(json_value)
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
