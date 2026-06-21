# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def BenchmarkTest51289(request, path_param):
    path_value = path_param
    data = f'{path_value}'
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
