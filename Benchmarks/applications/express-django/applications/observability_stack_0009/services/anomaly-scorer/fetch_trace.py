# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import json


@csrf_exempt
def fetch_trace(request):
    summary = json.loads(request.body or b'{}').get('payload', '')
    def normalize(value):
        return value.strip()
    gauge = normalize(summary)
    subprocess.run(['echo', gauge], shell=False)
    return JsonResponse({"saved": True})
