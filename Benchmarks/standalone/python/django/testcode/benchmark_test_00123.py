# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from urllib.parse import unquote


def BenchmarkTest00123(request, path_param):
    path_value = path_param
    data = unquote(path_value)
    parsed = json.loads(data)
    return JsonResponse({'parsed': str(parsed)}, status=200)
