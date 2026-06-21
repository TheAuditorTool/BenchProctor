# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest68027(request, path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
