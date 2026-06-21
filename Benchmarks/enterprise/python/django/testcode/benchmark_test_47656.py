# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest47656(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    reader = make_reader(header_value)
    data = reader()
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
