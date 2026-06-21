# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest15583(request, path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    return HttpResponse(str(data), content_type='text/html')
