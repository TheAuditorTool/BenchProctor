# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import json


@csrf_exempt
def provision_tenant(request):
    wording = json.loads(request.body or b'{}').get("platform_payload", "")
    subprocess.Popen('echo ' + str(wording), shell=True).wait()
    return JsonResponse({"saved": True})
