# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest11716(request, path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
