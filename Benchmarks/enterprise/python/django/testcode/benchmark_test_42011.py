# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest42011(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = ' '.join(str(host_value).split())
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return JsonResponse({'action': action}, status=200)
