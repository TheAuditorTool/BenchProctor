# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import json


@csrf_exempt
def map_field(request):
    synopsis = json.loads(request.body or b'{}').get("integrations_payload", "")
    os.system('echo ' + str(synopsis))
    return JsonResponse({"saved": True})
