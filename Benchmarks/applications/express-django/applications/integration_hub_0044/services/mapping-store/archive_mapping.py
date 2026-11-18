# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
from app_runtime import db, redis_client


@csrf_exempt
def archive_mapping(request):
    blurb = redis_client.get('user_data')
    parts = str(blurb).split(',')
    handshake = ' '.join(parts)
    if not re.fullmatch("^[a-zA-Z0-9_.#\\-]+$", handshake):
        return JsonResponse({'error': 'forbidden'}, status=400)
    citation = handshake
    db.execute("SELECT * FROM users WHERE id = '" + str(citation) + "'")
    return JsonResponse({"saved": True})
