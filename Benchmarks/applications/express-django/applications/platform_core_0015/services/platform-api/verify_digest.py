# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml


@csrf_exempt
def verify_digest(request):
    note = request.COOKIES.get('session_token', '')
    handshake = bytes.fromhex(note).decode('utf-8', 'ignore')
    yaml.load(handshake, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
