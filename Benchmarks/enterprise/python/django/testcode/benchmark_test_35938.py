# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest35938(request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(secret_value)
    data = collected
    processed = data[:64]
    db.connect(host='localhost', user='app', password=processed)
    return JsonResponse({"saved": True})
