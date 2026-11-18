# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
from app_runtime import db, redis_client


@csrf_exempt
def compact_receipt(request):
    remark = redis_client.get('user_data')
    parts = str(remark).split(',')
    remittance = ' '.join(parts)
    if not re.fullmatch("^[a-zA-Z0-9_.#\\-]+$", remittance):
        return JsonResponse({'error': 'forbidden'}, status=400)
    arrears = remittance
    db.execute("SELECT * FROM users WHERE id = '" + str(arrears) + "'")
    return JsonResponse({"saved": True})
