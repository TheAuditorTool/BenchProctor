# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def rotate_fulfillment(request):
    notice = request.META.get('HTTP_ORIGIN', '')
    backorder = f'{notice!s}'
    parsed = json.loads(backorder)
    return JsonResponse({'parsed': str(parsed)}, status=200)
