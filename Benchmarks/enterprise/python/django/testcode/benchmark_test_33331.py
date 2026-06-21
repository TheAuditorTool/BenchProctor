# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest33331(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    def _primary():
        return HttpResponse(Template(data).render(Context()))
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
