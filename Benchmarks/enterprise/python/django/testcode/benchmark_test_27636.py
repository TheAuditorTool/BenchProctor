# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def normalise_input(value):
    return value.strip()

def BenchmarkTest27636(request, path_param):
    path_value = path_param
    data = normalise_input(path_value)
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
