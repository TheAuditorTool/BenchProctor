# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest07145(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = default_blank(auth_header)
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return JsonResponse({'secret': str(secret)}, status=200)
