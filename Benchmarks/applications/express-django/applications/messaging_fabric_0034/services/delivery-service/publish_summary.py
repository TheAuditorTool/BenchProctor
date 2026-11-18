# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def publish_summary(request):
    footnote = request.POST.get('field', '')
    parts = []
    for token in str(footnote).split(','):
        parts.append(token.strip())
    bulletin = ','.join(parts)
    try:
        _coerced = int(bulletin)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    heading = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(heading))
    return JsonResponse({"saved": True})
