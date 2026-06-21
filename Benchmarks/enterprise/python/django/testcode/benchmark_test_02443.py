# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02443(request, path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
