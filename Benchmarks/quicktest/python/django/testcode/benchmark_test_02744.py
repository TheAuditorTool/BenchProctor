# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


def BenchmarkTest02744(request):
    user_id = request.GET.get('id', '')
    parts = []
    for token in str(user_id).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
