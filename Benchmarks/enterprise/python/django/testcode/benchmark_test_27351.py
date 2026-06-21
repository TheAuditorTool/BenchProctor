# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest27351(request):
    user_id = request.GET.get('id', '')
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(user_id),))
    return JsonResponse({'secret': str(secret)}, status=200)
