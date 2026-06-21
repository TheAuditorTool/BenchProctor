# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest49979(request, path_param):
    path_value = path_param
    data = '%s' % str(path_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    trusted_claim = str(processed)
    return JsonResponse({'trusted': trusted_claim}, status=200)
