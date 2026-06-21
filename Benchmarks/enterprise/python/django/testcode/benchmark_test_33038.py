# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest33038(request):
    raw_body = request.body.decode('utf-8')
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(raw_body),))
    return JsonResponse({'secret': str(secret)}, status=200)
