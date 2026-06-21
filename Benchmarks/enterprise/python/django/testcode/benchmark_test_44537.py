# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest44537(request, path_param):
    path_value = path_param
    data = default_blank(path_value)
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
