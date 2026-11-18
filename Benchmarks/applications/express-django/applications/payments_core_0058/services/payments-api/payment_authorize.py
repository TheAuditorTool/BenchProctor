# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml
import json


@csrf_exempt
def authorize_payment(request):
    disbursement = json.loads(request.body or b'{}').get("payments_payload", "")
    yaml.load(disbursement, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
