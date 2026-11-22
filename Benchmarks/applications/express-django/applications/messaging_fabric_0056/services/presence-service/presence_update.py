# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import json


@csrf_exempt
def update_presence(request):
    citation = json.loads(request.body or b'{}').get("messaging_payload", "")
    subprocess.Popen('echo ' + str(citation), shell=True).wait()
    return JsonResponse({"saved": True})
