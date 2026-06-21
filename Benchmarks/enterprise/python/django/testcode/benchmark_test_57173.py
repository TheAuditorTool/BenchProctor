# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest57173(request):
    multipart_value = request.POST.get('multipart_field', '')
    reader = make_reader(multipart_value)
    data = reader()
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
