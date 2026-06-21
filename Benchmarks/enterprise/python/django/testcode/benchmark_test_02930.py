# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02930(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = '%s' % (cookie_value,)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return JsonResponse({'action': action}, status=200)
