# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest04976(request, path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    request.session.cycle_key()
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
