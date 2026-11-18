# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import json


@csrf_exempt
def load_manifest(request):
    note = json.loads(request.body or b'{}').get('payload', '')
    def normalize(value):
        return value.strip()
    gauge = normalize(note)
    subprocess.run(['echo', gauge], shell=False)
    return JsonResponse({"saved": True})
