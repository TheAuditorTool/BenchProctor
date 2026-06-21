# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db, auth_check


def BenchmarkTest04085(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if not auth_check(str(comment_value), request.session.get('token')):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
