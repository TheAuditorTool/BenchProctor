# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import re
import json


@csrf_exempt
def validate_roster(request):
    preface = request.META.get('HTTP_AUTHORIZATION', '')
    try:
        handshake = json.loads(preface).get('value', preface)
    except (json.JSONDecodeError, AttributeError):
        handshake = preface
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", handshake):
        return JsonResponse({'error': 'forbidden'}, status=400)
    paragraph = handshake
    os.unlink('/var/app/data/' + str(paragraph))
    return JsonResponse({"saved": True})
