# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest24207(request, path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
