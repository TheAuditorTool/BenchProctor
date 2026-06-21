# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest25824(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(referer_value),))
    return JsonResponse({"saved": True})
