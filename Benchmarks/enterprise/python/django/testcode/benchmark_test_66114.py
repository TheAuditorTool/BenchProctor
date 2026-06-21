# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db, auth_check


request_state: dict[str, str] = {}

def BenchmarkTest66114(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    request_state['last_input'] = comment_value
    data = request_state['last_input']
    if not auth_check(str(data), request.session.get('token')):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
