# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest10687(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    ns = SimpleNamespace(payload=header_value)
    data = getattr(ns, 'payload')
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(data),))
    return JsonResponse({'record': str(record)}, status=200)
