# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest01634(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(processed),))
    return JsonResponse({"saved": True})
