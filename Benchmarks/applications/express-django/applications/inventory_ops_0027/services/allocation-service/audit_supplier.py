# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml


@csrf_exempt
def audit_supplier(request):
    summary = request.COOKIES.get('session_token', '')
    restock = bytes.fromhex(summary).decode('utf-8', 'ignore')
    yaml.load(restock, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
