# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest60811(request):
    cookie_value = request.COOKIES.get('session_token', '')
    reader = make_reader(cookie_value)
    data = reader()
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
