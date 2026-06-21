# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest16025(request, path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
