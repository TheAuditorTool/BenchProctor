# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest26253(request, path_param):
    path_value = path_param
    digest = hashlib.sha1(str(path_value).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
