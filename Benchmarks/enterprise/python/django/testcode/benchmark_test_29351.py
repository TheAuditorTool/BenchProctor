# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest29351(request, path_param):
    path_value = path_param
    data = '%s' % (path_value,)
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
