# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest37425(request, path_param):
    path_value = path_param
    request.session.set_expiry(1800)
    request.session['data'] = str(path_value)
    return JsonResponse({"saved": True})
