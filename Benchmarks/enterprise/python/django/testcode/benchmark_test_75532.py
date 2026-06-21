# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest75532(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = '%s' % str(cookie_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
