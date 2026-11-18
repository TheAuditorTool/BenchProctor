# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def authorize_payment(request):
    remittance = json.loads(request.body or b'{}').get("payments_payload", "")
    parsed = json.loads(remittance)
    return JsonResponse({'parsed': str(parsed)}, status=200)
