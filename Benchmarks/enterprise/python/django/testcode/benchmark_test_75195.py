# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest75195(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    pending = list(str(auth_header).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
