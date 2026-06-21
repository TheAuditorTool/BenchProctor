# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest55928(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    db.execute('SELECT * FROM users WHERE id = :id', {'id': data})
    return JsonResponse({"saved": True})
