# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09313(request, path_param):
    path_value = path_param
    request.session['data'] = str(path_value)
    return JsonResponse({"saved": True})
