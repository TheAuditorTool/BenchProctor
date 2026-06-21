# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest65231(request, path_param):
    path_value = path_param
    eval(str(path_value))
    return JsonResponse({"saved": True})
