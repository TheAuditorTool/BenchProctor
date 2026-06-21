# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest43463(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ns = SimpleNamespace(payload=comment_value)
    data = getattr(ns, 'payload')
    def _primary():
        with open('/var/uploads/' + str(data), 'wb') as fh:
            fh.write(b'data')
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return JsonResponse({"saved": True})
