# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest06099(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(forwarded_ip),))
    return JsonResponse({"saved": True})
