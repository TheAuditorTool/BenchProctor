# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest49136(request, path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        return JsonResponse({'error': 'privilege drop failed'}, status=500)
    return JsonResponse({"saved": True})
