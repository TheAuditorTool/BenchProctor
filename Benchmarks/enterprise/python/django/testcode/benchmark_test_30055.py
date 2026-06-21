# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest30055(request, path_param):
    path_value = path_param
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    request.session.cycle_key()
    request.session['user'] = str(path_value)
    return JsonResponse({"saved": True})
