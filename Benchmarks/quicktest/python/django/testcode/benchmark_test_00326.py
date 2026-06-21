# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote


def BenchmarkTest00326(request, path_param):
    path_value = path_param
    data = unquote(path_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
