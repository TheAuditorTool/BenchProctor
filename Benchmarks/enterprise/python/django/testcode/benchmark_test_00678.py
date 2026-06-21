# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest00678(request, path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
