# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00702(request, path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid number'}, status=400)
    processed = _coerced
    eval(str(processed))
    return JsonResponse({"saved": True})
