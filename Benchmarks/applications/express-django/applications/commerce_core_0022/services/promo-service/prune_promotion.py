# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def prune_promotion(request):
    subject = request.META.get('HTTP_ORIGIN', '')
    voucher = f'{subject!s}'
    parsed = json.loads(voucher)
    return JsonResponse({'parsed': str(parsed)}, status=200)
