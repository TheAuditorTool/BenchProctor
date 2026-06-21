# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest34316(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    processed = data[:64]
    db.users.find({'$where': "this.username == '" + str(processed) + "'"})
    return JsonResponse({"saved": True})
