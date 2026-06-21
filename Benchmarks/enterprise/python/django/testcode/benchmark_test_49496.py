# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest49496(request, path_param):
    path_value = path_param
    if path_value not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = path_value
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
