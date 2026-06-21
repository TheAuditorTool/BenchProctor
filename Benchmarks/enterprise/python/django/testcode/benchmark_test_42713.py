# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest42713(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    request_state['last_input'] = comment_value
    data = request_state['last_input']
    def _primary():
        return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
