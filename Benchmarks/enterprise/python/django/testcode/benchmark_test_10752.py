# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest10752(request):
    host_value = request.META.get('HTTP_HOST', '')
    parts = []
    for token in str(host_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return JsonResponse({'action': action}, status=200)
