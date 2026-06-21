# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from types import SimpleNamespace
from app_runtime import auth_check


def BenchmarkTest74335(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    if not auth_check(str(data), request.session.get('token')):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
