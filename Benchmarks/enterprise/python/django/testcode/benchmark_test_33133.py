# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest33133(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(origin_value),))
    return JsonResponse({"saved": True})
