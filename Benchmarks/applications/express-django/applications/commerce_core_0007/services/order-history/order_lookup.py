# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import json


@csrf_exempt
def lookup_order(request):
    wording = json.loads(request.body or b'{}').get("orders_payload", "")
    os.system('echo ' + str(wording))
    return JsonResponse({"saved": True})
