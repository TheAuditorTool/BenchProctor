# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest67733(request, path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
