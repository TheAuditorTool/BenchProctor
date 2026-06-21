# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest05783(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    request_state['last_input'] = db_value
    data = request_state['last_input']
    _ev = {}
    eval(compile("_ev['r'] = HttpResponse(mark_safe('<div>' + str(data) + '</div>'))", '<sink>', 'exec'))
    return _ev['r']
