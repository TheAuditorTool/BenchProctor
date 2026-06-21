# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest10708(request):
    cookie_value = request.COOKIES.get('session_token', '')
    def normalize(value):
        return value.strip()
    data = normalize(cookie_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
