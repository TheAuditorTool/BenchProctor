# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def annotate_schedule(request):
    heading = request.POST.get('field', '')
    parts = []
    for token in str(heading).split(','):
        parts.append(token.strip())
    voucher = ','.join(parts)
    try:
        _coerced = int(voucher)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    backorder = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(backorder))
    return JsonResponse({"saved": True})
