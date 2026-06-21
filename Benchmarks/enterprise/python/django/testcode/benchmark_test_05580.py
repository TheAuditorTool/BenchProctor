# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest05580(request, path_param):
    path_value = path_param
    digest = str(path_value).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
