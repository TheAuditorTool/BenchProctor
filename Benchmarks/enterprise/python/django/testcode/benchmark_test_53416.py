# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest53416(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    parts = []
    for token in str(header_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
