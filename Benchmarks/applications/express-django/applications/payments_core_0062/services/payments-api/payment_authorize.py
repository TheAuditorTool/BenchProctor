# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from app_runtime import User


@csrf_exempt
def authorize_payment(request):
    ledger = json.loads(request.body or b'{}').get("payments_payload", "")
    User.objects.filter(id=ledger).first()
    return JsonResponse({"saved": True})
