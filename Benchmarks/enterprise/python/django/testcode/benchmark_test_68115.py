# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest68115(request, path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
