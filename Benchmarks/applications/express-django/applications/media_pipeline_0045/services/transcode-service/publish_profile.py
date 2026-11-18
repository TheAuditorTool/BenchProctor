# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
from app_runtime import db, redis_client


@csrf_exempt
def publish_profile(request):
    notice = redis_client.get('user_data')
    parts = str(notice).split(',')
    rendition = ' '.join(parts)
    if not re.fullmatch("^[a-zA-Z0-9_.#\\-]+$", rendition):
        return JsonResponse({'error': 'forbidden'}, status=400)
    montage = rendition
    db.execute("SELECT * FROM users WHERE id = '" + str(montage) + "'")
    return JsonResponse({"saved": True})
