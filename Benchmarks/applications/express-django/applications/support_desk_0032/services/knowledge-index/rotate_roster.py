# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
from app_runtime import db, redis_client


@csrf_exempt
def rotate_roster(request):
    note = redis_client.get('user_data')
    parts = str(note).split(',')
    inquiry = ' '.join(parts)
    if not re.fullmatch("^[a-zA-Z0-9_.#\\-]+$", inquiry):
        return JsonResponse({'error': 'forbidden'}, status=400)
    grievance = inquiry
    db.execute("SELECT * FROM users WHERE id = '" + str(grievance) + "'")
    return JsonResponse({"saved": True})
