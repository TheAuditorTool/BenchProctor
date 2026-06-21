# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest69329(request, path_param):
    path_value = path_param
    data = '%s' % str(path_value)
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
