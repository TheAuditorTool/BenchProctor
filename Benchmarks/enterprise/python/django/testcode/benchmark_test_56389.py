# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest56389(request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data = secret_value if secret_value else 'default'
    db.connect(host='localhost', user='app', password=data)
    return JsonResponse({"saved": True})
