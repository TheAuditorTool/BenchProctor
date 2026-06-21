# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest80779(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return JsonResponse({"saved": True})
