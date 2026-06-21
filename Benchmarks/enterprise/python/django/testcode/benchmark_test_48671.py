# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest48671(request, path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    request.session.cycle_key()
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
