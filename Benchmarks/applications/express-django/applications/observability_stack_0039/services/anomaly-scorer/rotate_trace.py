# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import json


@csrf_exempt
def rotate_trace(request):
    caption = json.loads(request.body or b'{}').get('payload', '')
    def normalize(value):
        return value.strip()
    cohort = normalize(caption)
    subprocess.run(['echo', cohort], shell=False)
    return JsonResponse({"saved": True})
