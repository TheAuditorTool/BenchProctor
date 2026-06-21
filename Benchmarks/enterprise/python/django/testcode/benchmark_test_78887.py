# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest78887(request, path_param):
    path_value = path_param
    data = '%s' % (path_value,)
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
