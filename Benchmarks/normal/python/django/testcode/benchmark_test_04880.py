# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db, auth_check


def BenchmarkTest04880(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if not auth_check(request.session.get('user', ''), str(comment_value)):
        return JsonResponse({'error': 'forbidden'}, status=403)
    return JsonResponse({"saved": True})
