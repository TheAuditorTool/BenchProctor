# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from app_runtime import db


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest31483(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = handle(db_value)
    _ev = {}
    eval(compile('_ev[\'r\'] = HttpResponse(mark_safe(\'<img src="\' + str(data) + \'">\'))', '<sink>', 'exec'))
    return _ev['r']
