# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest24515(request, path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    return HttpResponse(str(data), content_type='text/html')
