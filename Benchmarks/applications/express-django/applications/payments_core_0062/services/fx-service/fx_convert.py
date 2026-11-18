# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
import json


@csrf_exempt
def convert_fx(request):
    ledger = json.loads(request.body or b'{}').get("payments_payload", "")
    requests.get(str(ledger))
    return JsonResponse({"saved": True})
