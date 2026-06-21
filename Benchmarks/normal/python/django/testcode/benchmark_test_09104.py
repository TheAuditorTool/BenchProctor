# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09104(request, path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    request.session.cycle_key()
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
