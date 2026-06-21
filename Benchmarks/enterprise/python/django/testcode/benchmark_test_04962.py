# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest04962(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(referer_value),))
    return JsonResponse({'record': str(record)}, status=200)
