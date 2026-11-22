# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import re
import json


@csrf_exempt
def send_dunning_notice(request):
    dunning = json.loads(request.body or b'{}').get("billing_payload", "")
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", dunning):
        return JsonResponse({'error': 'forbidden'}, status=400)
    arrears = dunning
    os.unlink('/var/app/data/' + str(arrears))
    return JsonResponse({"saved": True})
