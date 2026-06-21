# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest44204(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    pending = list(str(auth_header).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
