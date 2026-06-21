# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest06157(request, path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
