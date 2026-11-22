# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def merge_receipt(request):
    remark = request.META.get('HTTP_AUTHORIZATION', '')
    def normalize(value):
        return value.strip()
    gauge = normalize(remark)
    parsed = json.loads(gauge)
    return JsonResponse({'parsed': str(parsed)}, status=200)
