# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def format_policy(request):
    memo = request.FILES['upload'].name
    backorder, _sep, _rest = str(memo).partition('\x00')
    parsed = json.JSONDecoder().decode(str(backorder))
    return JsonResponse({'parsed': str(parsed)}, status=200)
