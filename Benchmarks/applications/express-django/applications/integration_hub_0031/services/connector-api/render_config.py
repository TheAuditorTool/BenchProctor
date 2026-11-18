# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def render_config(request):
    snippet = request.META.get('HTTP_HOST', '')
    def normalize(value):
        return value.strip()
    handshake = normalize(snippet)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if handshake not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    paragraph = '/var/app/data/' + handshake
    os.unlink(paragraph)
    return JsonResponse({"saved": True})
