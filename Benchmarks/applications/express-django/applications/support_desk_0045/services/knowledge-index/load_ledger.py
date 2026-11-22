# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def load_ledger(request):
    remark = request.META.get('HTTP_AUTHORIZATION', '')
    def normalize(value):
        return value.strip()
    inquiry = normalize(remark)
    parsed = json.loads(inquiry)
    return JsonResponse({'parsed': str(parsed)}, status=200)
