# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest80345(request, path_param):
    path_value = path_param
    data = '%s' % (path_value,)
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    request.session.cycle_key()
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
