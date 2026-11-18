# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import re
import json


@csrf_exempt
def publish_config(request):
    notice = request.META.get('HTTP_AUTHORIZATION', '')
    try:
        persona = json.loads(notice).get('value', notice)
    except (json.JSONDecodeError, AttributeError):
        persona = notice
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", persona):
        return JsonResponse({'error': 'forbidden'}, status=400)
    handshake = persona
    os.unlink('/var/app/data/' + str(handshake))
    return JsonResponse({"saved": True})
