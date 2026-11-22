# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def merge_digest(request):
    memo = request.META.get('HTTP_ORIGIN', '')
    ledger = f'{memo!s}'
    parsed = json.loads(ledger)
    return JsonResponse({'parsed': str(parsed)}, status=200)
