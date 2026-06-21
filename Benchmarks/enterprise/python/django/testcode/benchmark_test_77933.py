# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote


def BenchmarkTest77933(request, path_param):
    path_value = path_param
    data = unquote(path_value)
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
