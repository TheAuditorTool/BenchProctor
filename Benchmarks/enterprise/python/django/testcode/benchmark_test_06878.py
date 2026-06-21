# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def to_text(value):
    return str(value).strip()

def BenchmarkTest06878(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = to_text(cookie_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
