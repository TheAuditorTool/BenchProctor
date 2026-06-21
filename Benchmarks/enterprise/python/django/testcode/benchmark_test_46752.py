# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest46752(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    eval(compile('db.users.find({\'$where\': "this.username == \'" + str(data) + "\'"})', '<sink>', 'exec'))
    return JsonResponse({"saved": True})
