# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest72668(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    request_state['last_input'] = comment_value
    data = request_state['last_input']
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
