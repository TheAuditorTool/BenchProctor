# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest51877(request, path_param):
    path_value = path_param
    trusted_claim = str(path_value)
    return JsonResponse({'trusted': trusted_claim}, status=200)
