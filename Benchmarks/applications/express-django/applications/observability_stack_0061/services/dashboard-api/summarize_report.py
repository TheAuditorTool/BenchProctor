# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def summarize_report(request):
    headline = request.POST.get('field', '')
    parts = []
    for token in str(headline).split(','):
        parts.append(token.strip())
    cohort = ','.join(parts)
    try:
        _coerced = int(cohort)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    gauge = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(gauge))
    return JsonResponse({"saved": True})
