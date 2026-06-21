# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
from urllib.parse import unquote


def BenchmarkTest56718(request, path_param):
    path_value = path_param
    data = unquote(path_value)
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return JsonResponse({'token': str(token)}, status=200)
