# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest72235(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = host_value if host_value else 'default'
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return JsonResponse({'action': action}, status=200)
