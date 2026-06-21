# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest39762(request):
    user_id = request.GET.get('id', '')
    data = ' '.join(str(user_id).split())
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return JsonResponse({"saved": True})
