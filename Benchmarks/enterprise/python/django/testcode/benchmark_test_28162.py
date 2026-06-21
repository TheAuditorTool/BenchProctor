# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest28162(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = '%s' % str(ua_value)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return JsonResponse({'action': action}, status=200)
