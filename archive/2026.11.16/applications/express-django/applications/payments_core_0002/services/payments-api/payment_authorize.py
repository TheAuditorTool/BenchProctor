# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from app_runtime import db


@csrf_exempt
def authorize_payment(request):
    disbursement = json.loads(request.body or b'{}').get("payments_payload", "")
    db.execute("SELECT * FROM users WHERE id = '" + str(disbursement) + "'")
    return JsonResponse({"saved": True})
