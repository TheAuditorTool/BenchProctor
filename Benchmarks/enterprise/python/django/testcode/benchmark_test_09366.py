# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09366(request):
    user_id = request.GET.get('id', '')
    parts = []
    for token in str(user_id).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
