# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import subprocess


@csrf_exempt
def run_reconciliation(request):
    ledger = json.loads(request.body or b'{}').get("payments_payload", "")
    subprocess.run(['echo', ledger], shell=False)
    return JsonResponse({"saved": True})
