# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest02769(request, path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
