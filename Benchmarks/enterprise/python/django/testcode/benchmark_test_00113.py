# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from types import SimpleNamespace


def BenchmarkTest00113(request):
    raw_body = request.body.decode('utf-8')
    ns = SimpleNamespace(payload=raw_body)
    data = getattr(ns, 'payload')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
