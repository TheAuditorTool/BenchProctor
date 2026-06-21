# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from urllib.parse import unquote


def BenchmarkTest63963(request, path_param):
    path_value = path_param
    data = unquote(path_value)
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
