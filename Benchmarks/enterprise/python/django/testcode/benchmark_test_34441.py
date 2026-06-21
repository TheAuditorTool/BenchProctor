# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def coalesce_blank(value):
    return value or ''

def BenchmarkTest34441(request, path_param):
    path_value = path_param
    data = coalesce_blank(path_value)
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
