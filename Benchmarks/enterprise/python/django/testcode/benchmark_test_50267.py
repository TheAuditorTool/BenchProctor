# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest50267(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = f'{ua_value}'
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(data),))
    return JsonResponse({"saved": True})
