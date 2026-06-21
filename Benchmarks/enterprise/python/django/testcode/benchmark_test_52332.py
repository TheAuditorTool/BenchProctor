# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def BenchmarkTest52332(request, path_param):
    path_value = path_param
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
