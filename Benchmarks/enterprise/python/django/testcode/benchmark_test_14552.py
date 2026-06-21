# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest14552(request, path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
