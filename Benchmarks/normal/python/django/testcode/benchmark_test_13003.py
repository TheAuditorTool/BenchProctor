# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest13003(request):
    host_value = request.META.get('HTTP_HOST', '')
    reader = make_reader(host_value)
    data = reader()
    return HttpResponse(str(data), content_type='text/html')
