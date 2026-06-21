# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest53750(request, path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
