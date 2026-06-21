# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from types import SimpleNamespace


def BenchmarkTest11729(request):
    user_id = request.GET.get('id', '')
    ns = SimpleNamespace(payload=user_id)
    data = getattr(ns, 'payload')
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
