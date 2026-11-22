# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def resolve_config(request):
    headline = request.META.get('HTTP_ORIGIN', '')
    disbursement = f'{headline!s}'
    parsed = json.loads(disbursement)
    return JsonResponse({'parsed': str(parsed)}, status=200)
