# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def to_text(value):
    return str(value).strip()

def BenchmarkTest09278(request, path_param):
    path_value = path_param
    data = to_text(path_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
