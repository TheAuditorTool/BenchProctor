# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import json


@csrf_exempt
def ingest_metric(request):
    heading = json.loads(request.body or b'{}').get("telemetry_payload", "")
    subprocess.run(['echo', heading], shell=False)
    return JsonResponse({"saved": True})
