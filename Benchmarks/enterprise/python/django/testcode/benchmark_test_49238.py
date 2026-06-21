# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest49238(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return JsonResponse({'secret': str(secret)}, status=200)
