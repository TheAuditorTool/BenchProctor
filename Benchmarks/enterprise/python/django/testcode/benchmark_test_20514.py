# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest20514(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = str(host_value).replace('\x00', '')
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return JsonResponse({'action': action}, status=200)
