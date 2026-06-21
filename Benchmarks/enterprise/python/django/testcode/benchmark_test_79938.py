# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest79938(request, path_param):
    path_value = path_param
    data = f'{path_value}'
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
