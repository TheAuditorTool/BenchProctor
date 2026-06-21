# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest56727(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    def normalize(value):
        return value.strip()
    data = normalize(header_value)
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(data),))
    return JsonResponse({'record': str(record)}, status=200)
