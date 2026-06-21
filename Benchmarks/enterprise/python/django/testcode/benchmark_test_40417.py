# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest40417(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    _ev = {}
    eval(compile('_ev[\'r\'] = HttpResponse(\'<script src="\' + str(data) + \'"></script>\', content_type=\'text/html\')', '<sink>', 'exec'))
    return _ev['r']
