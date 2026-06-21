# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
from urllib.parse import unquote


def BenchmarkTest01005(request, path_param):
    path_value = path_param
    data = unquote(path_value)
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
