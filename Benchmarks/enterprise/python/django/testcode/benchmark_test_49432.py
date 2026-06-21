# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest49432(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    def normalize(value):
        return value.strip()
    data = normalize(forwarded_ip)
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(data),))
    return JsonResponse({'record': str(record)}, status=200)
