# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest30916(request, path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    return HttpResponse('<html><body><h1>' + str(data) + '</h1></body></html>', content_type='text/html')
