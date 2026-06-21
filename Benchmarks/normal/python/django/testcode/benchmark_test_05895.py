# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest05895(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value:.200s}'
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return JsonResponse({"saved": True})
