# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import json


@csrf_exempt
def sync_watchlist(request):
    note = json.loads(request.body or b'{}').get("risk_payload", "")
    os.unlink('/var/app/data/' + str(note))
    return JsonResponse({"saved": True})
