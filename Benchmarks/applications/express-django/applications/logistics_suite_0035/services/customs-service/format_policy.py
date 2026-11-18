# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def format_policy(request):
    phrase = request.POST.get('field', '')
    parts = []
    for token in str(phrase).split(','):
        parts.append(token.strip())
    parcel = ','.join(parts)
    try:
        _coerced = int(parcel)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    consignment = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(consignment))
    return JsonResponse({"saved": True})
