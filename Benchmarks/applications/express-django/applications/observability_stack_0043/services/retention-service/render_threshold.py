# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
from app_runtime import db, redis_client


@csrf_exempt
def render_threshold(request):
    note = redis_client.get('user_data')
    parts = str(note).split(',')
    gauge = ' '.join(parts)
    if not re.fullmatch("^[a-zA-Z0-9_.#\\-]+$", gauge):
        return JsonResponse({'error': 'forbidden'}, status=400)
    cohort = gauge
    db.execute("SELECT * FROM users WHERE id = '" + str(cohort) + "'")
    return JsonResponse({"saved": True})
