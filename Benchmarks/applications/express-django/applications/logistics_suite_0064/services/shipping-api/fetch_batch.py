# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import json


@csrf_exempt
def fetch_batch(request):
    transcript = json.loads(request.body or b'{}').get('payload', '')
    def normalize(value):
        return value.strip()
    parcel = normalize(transcript)
    subprocess.run(['echo', parcel], shell=False)
    return JsonResponse({"saved": True})
