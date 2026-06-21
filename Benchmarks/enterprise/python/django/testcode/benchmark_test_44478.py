# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest44478(request):
    host_value = request.META.get('HTTP_HOST', '')
    prefix = ''
    data = prefix + str(host_value)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return JsonResponse({'action': action}, status=200)
