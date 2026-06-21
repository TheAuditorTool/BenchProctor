# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest28992(request):
    cookie_value = request.COOKIES.get('session_token', '')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
