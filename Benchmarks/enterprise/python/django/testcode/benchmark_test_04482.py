# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest04482(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    _ev = {}
    eval(compile('_ev[\'r\'] = HttpResponse(mark_safe(\'<img src="\' + str(data) + \'">\'))', '<sink>', 'exec'))
    return _ev['r']
