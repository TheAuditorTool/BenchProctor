# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import json


@csrf_exempt
def extract_caption(request):
    note = json.loads(request.body or b'{}').get("media_payload", "")
    subprocess.run('echo ' + str(note), shell=True)
    return JsonResponse({"saved": True})
