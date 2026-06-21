# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest03592(request):
    user_id = request.GET.get('id', '')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(user_id),))
    return JsonResponse({"saved": True})
