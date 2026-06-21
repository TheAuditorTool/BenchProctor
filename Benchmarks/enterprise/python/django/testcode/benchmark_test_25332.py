# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest25332(request, path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
