# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest49683(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    kind = 'json' if str(origin_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = origin_value
            data = parsed
        case _:
            data = origin_value
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return JsonResponse({"saved": True})
