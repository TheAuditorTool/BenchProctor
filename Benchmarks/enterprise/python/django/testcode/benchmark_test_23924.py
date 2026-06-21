# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest23924(request):
    user_id = request.GET.get('id', '')
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(user_id),))
    return JsonResponse({"saved": True})
