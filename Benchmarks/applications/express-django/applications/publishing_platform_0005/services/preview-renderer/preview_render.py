# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import json


@csrf_exempt
def render_preview(request):
    paragraph = json.loads(request.body or b'{}').get("publishing_payload", "")
    subprocess.Popen('echo ' + str(paragraph), shell=True).wait()
    return JsonResponse({"saved": True})
