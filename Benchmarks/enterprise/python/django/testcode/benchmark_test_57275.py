# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
from app_runtime import db


def BenchmarkTest57275(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(data),))
    return JsonResponse({"saved": True})
