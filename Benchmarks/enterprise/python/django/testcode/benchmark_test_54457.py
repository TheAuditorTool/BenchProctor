# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest54457(request):
    host_value = request.META.get('HTTP_HOST', '')
    pending = list(str(host_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
