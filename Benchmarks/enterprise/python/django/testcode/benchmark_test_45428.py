# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest45428(request, path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    values = str(data).split(',')
    if values:
        return JsonResponse({'first': values[0], 'dropped': len(values) - 1}, status=200)
    return JsonResponse({"saved": True})
