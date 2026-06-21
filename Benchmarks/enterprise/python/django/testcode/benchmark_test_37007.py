# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest37007(request, path_param):
    path_value = path_param
    parts = []
    for token in str(path_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    int(str(data))
    return JsonResponse({"saved": True})
