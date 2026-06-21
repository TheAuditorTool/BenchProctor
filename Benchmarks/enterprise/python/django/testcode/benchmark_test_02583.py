# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02583(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
