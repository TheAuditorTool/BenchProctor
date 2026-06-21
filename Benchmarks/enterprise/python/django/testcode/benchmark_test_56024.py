# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest56024(request, path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
