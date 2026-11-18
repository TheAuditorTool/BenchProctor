# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def compact_bundle(request):
    snippet = request.META.get('HTTP_HOST', '')
    def normalize(value):
        return value.strip()
    persona = normalize(snippet)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if persona not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    handshake = '/var/app/data/' + persona
    os.unlink(handshake)
    return JsonResponse({"saved": True})
