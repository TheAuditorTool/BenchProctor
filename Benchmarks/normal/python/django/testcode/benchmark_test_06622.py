# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest06622(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
