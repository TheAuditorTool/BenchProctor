# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import socket
from types import SimpleNamespace


def BenchmarkTest02597(request):
    cookie_value = request.COOKIES.get('session_token', '')
    ns = SimpleNamespace(payload=cookie_value)
    data = getattr(ns, 'payload')
    if os.environ.get("APP_ENV", "production") != "test":
        s = socket.create_connection((str(data), 80))
        s.close()
    return JsonResponse({"saved": True})
