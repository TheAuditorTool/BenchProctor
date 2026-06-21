# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest35921(request, path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
