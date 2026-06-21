# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest29425(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    eval(str(data))
    return JsonResponse({"saved": True})
