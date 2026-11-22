# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def prune_webhook(request):
    heading = request.META.get('HTTP_ORIGIN', '')
    handshake = f'{heading!s}'
    parsed = json.loads(handshake)
    return JsonResponse({'parsed': str(parsed)}, status=200)
