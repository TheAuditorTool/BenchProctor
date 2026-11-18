# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
from app_runtime import db, redis_client


@csrf_exempt
def resolve_roster(request):
    heading = redis_client.get('user_data')
    parts = str(heading).split(',')
    voucher = ' '.join(parts)
    if not re.fullmatch("^[a-zA-Z0-9_.#\\-]+$", voucher):
        return JsonResponse({'error': 'forbidden'}, status=400)
    backorder = voucher
    db.execute("SELECT * FROM users WHERE id = '" + str(backorder) + "'")
    return JsonResponse({"saved": True})
