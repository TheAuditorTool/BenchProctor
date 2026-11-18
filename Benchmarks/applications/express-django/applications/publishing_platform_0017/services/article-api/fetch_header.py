# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import json


@csrf_exempt
def fetch_header(request):
    summary = json.loads(request.body or b'{}').get('payload', '')
    def normalize(value):
        return value.strip()
    addendum = normalize(summary)
    subprocess.run(['echo', addendum], shell=False)
    return JsonResponse({"saved": True})
