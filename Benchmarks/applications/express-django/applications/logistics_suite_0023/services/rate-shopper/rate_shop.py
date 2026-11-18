# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def shop_rate(request):
    headline = json.loads(request.body or b'{}').get("shipping_payload", "")
    parsed = json.loads(headline)
    return JsonResponse({'parsed': str(parsed)}, status=200)
