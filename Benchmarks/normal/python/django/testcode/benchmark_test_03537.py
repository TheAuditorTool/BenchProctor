# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03537(request, path_param):
    path_value = path_param
    data = f'{path_value}'
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
