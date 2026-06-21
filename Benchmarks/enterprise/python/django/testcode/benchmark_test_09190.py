# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest09190(request, path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return JsonResponse({'validated': str(data)}, status=200)
    return JsonResponse({"saved": True})
