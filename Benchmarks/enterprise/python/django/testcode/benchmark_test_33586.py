# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest33586(request):
    host_value = request.META.get('HTTP_HOST', '')
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(host_value),))
    return JsonResponse({'secret': str(secret)}, status=200)
