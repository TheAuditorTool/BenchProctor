# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote


def BenchmarkTest10889(request, path_param):
    path_value = path_param
    data = unquote(path_value)
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
