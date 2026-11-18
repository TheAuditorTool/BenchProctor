# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
from app_runtime import db, redis_client


@csrf_exempt
def build_roster(request):
    passage = redis_client.get('user_data')
    parts = str(passage).split(',')
    montage = ' '.join(parts)
    if not re.fullmatch("^[a-zA-Z0-9_.#\\-]+$", montage):
        return JsonResponse({'error': 'forbidden'}, status=400)
    rendition = montage
    db.execute("SELECT * FROM users WHERE id = '" + str(rendition) + "'")
    return JsonResponse({"saved": True})
