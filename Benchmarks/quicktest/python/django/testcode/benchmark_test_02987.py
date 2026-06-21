# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02987(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    parts = []
    for token in str(auth_header).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
