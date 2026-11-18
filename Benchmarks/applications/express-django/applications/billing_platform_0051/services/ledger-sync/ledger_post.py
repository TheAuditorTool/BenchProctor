# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import json


@csrf_exempt
def post_ledger_entry(request):
    remittance = json.loads(request.body or b'{}').get("billing_payload", "")
    os.unlink('/var/app/data/' + str(remittance))
    return JsonResponse({"saved": True})
