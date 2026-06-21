# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest12159(request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data = str(secret_value).replace('\x00', '')
    db.connect(host='localhost', user='app', password=data)
    return JsonResponse({"saved": True})
