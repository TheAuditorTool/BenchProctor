# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest61220(request):
    secret_value = 'config_secret_test_abc123'
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(secret_value)
    data = collected
    db.connect(host='localhost', user='app', password=data)
    return JsonResponse({"saved": True})
