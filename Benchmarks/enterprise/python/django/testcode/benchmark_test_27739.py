# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest27739(request, path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
