# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def validate_webhook(request):
    snippet = request.META.get('HTTP_AUTHORIZATION', '')
    kind = 'json' if str(snippet).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            handshake = str(snippet).strip()
        case _:
            handshake = str(snippet)
    os.unlink('/var/app/data/' + str(handshake))
    return JsonResponse({"saved": True})
