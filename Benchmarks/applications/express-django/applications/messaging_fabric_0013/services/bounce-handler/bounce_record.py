# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import json


@csrf_exempt
def record_bounce(request):
    wording = json.loads(request.body or b'{}').get("messaging_payload", "")
    os.unlink('/var/app/data/' + str(wording))
    return JsonResponse({"saved": True})
