# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest01653(request, path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
