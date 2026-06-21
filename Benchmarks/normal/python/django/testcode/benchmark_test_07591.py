# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def coalesce_blank(value):
    return value or ''

def BenchmarkTest07591(request):
    secret_value = 'config_secret_test_abc123'
    data = coalesce_blank(secret_value)
    db.connect(host='localhost', user='app', password=data)
    return JsonResponse({"saved": True})
