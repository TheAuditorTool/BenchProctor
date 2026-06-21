# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest03338(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    reader = make_reader(origin_value)
    data = reader()
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
