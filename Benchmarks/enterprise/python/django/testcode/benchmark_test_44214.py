# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def normalise_input(value):
    return value.strip()

def BenchmarkTest44214(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = normalise_input(auth_header)
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return JsonResponse({'secret': str(secret)}, status=200)
