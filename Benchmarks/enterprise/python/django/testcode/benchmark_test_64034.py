# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest64034(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    request.session.cycle_key()
    request.session['user'] = str(comment_value)
    return JsonResponse({"saved": True})
