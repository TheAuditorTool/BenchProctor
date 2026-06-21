# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00749(request, path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
