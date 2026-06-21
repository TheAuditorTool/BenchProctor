# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest45532(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    reader = make_reader(referer_value)
    data = reader()
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
