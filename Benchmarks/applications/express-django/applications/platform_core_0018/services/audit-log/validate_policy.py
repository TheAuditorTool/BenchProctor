# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def validate_policy(request):
    subtitle = request.META.get('HTTP_USER_AGENT', '')
    def normalize(value):
        return value.strip()
    persona = normalize(subtitle)
    if persona not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    handshake = persona
    os.system('echo ' + str(handshake))
    return JsonResponse({"saved": True})
