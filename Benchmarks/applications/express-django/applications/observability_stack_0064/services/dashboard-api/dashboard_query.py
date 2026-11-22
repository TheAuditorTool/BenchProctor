# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import json


@csrf_exempt
def query_dashboard(request):
    paragraph = json.loads(request.body or b'{}').get("telemetry_payload", "")
    os.system('echo ' + str(paragraph))
    return JsonResponse({"saved": True})
