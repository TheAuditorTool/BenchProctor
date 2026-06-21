# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def BenchmarkTest51156(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
