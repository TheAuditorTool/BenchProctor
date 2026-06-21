# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import os


def BenchmarkTest46813(request):
    raw_body = request.body.decode('utf-8')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(raw_body)
    data = collected
    if os.environ.get("APP_ENV", "production") != "test":
        return redirect(str(data))
    return JsonResponse({"saved": True})
