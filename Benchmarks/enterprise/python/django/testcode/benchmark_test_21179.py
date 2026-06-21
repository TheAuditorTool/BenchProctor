# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest21179(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = '%s' % (cookie_value,)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
