# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import json


@csrf_exempt
def pull_supplier_feed(request):
    preface = json.loads(request.body or b'{}').get("inventory_payload", "")
    subprocess.run('echo ' + str(preface), shell=True)
    return JsonResponse({"saved": True})
