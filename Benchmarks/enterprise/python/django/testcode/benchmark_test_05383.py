# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest05383(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = f'{auth_header}'
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return JsonResponse({"saved": True})
