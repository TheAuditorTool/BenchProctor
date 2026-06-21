# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest22111(request):
    user_id = request.GET.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    def _primary():
        db.users.find({'$where': "this.username == '" + str(data) + "'"})
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return JsonResponse({"saved": True})
