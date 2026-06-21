# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def normalise_input(value):
    return value.strip()

def BenchmarkTest25926(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = normalise_input(cookie_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
