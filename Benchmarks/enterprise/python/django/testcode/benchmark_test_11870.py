# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def BenchmarkTest11870(request, path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
