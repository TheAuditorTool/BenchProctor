# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest53084(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = str(ua_value).replace('\x00', '')
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(data),))
    return JsonResponse({'record': str(record)}, status=200)
