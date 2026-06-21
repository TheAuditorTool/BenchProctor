# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest54444(request, path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
