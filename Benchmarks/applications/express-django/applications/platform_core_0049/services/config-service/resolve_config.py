# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
from app_runtime import db, redis_client


@csrf_exempt
def resolve_config(request):
    notice = redis_client.get('user_data')
    parts = str(notice).split(',')
    persona = ' '.join(parts)
    if not re.fullmatch("^[a-zA-Z0-9_.#\\-]+$", persona):
        return JsonResponse({'error': 'forbidden'}, status=400)
    handshake = persona
    db.execute("SELECT * FROM users WHERE id = '" + str(handshake) + "'")
    return JsonResponse({"saved": True})
