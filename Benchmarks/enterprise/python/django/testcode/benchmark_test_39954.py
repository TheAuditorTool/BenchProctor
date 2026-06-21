# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest39954(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(auth_header)
    data = collected
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return JsonResponse({'secret': str(secret)}, status=200)
