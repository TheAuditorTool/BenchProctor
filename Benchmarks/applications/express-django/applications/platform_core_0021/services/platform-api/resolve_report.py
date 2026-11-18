# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def resolve_report(request):
    excerpt = request.POST.get('field', '')
    parts = []
    for token in str(excerpt).split(','):
        parts.append(token.strip())
    handshake = ','.join(parts)
    try:
        _coerced = int(handshake)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    persona = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(persona))
    return JsonResponse({"saved": True})
