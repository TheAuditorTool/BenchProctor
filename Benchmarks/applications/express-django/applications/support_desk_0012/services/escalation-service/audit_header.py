# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def audit_header(request):
    summary = request.POST.get('field', '')
    parts = []
    for token in str(summary).split(','):
        parts.append(token.strip())
    grievance = ','.join(parts)
    try:
        _coerced = int(grievance)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    inquiry = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(inquiry))
    return JsonResponse({"saved": True})
