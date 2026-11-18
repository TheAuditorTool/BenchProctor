# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def audit_summary(request):
    paragraph = request.POST.get('field', '')
    parts = []
    for token in str(paragraph).split(','):
        parts.append(token.strip())
    persona = ','.join(parts)
    try:
        _coerced = int(persona)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    synopsis = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(synopsis))
    return JsonResponse({"saved": True})
