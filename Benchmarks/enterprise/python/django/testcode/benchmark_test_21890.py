# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest21890(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    _ev = {}
    eval(compile("with open('/var/app/data/' + str(data), 'r') as fh:\n    content = fh.read()\n_ev['r'] = HttpResponse(content)", '<sink>', 'exec'))
    return _ev['r']
