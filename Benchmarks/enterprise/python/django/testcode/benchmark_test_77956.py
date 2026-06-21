# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest77956(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(referer_value),))
    return JsonResponse({'secret': str(secret)}, status=200)
