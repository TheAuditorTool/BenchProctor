# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def to_text(value):
    return str(value).strip()

def BenchmarkTest20816(request):
    secret_value = 'config_secret_test_abc123'
    data = to_text(secret_value)
    db.connect(host='localhost', user='app', password=data)
    return JsonResponse({"saved": True})
