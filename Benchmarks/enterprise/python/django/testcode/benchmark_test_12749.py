# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest12749(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = f'{cookie_value:.200s}'
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
