# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest72929(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    def _primary():
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return HttpResponse(content)
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
