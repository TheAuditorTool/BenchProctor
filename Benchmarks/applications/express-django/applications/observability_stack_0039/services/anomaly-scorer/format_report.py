# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
from app_runtime import db, redis_client


@csrf_exempt
def format_report(request):
    caption = redis_client.get('user_data')
    parts = str(caption).split(',')
    cohort = ' '.join(parts)
    if not re.fullmatch("^[a-zA-Z0-9_.#\\-]+$", cohort):
        return JsonResponse({'error': 'forbidden'}, status=400)
    gauge = cohort
    db.execute("SELECT * FROM users WHERE id = '" + str(gauge) + "'")
    return JsonResponse({"saved": True})
