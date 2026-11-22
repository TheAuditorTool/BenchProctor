# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def prune_config(request):
    memo = request.FILES['upload'].name
    verdict, _sep, _rest = str(memo).partition('\x00')
    parsed = json.JSONDecoder().decode(str(verdict))
    return JsonResponse({'parsed': str(parsed)}, status=200)
