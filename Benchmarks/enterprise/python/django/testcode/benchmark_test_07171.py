# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest07171(request, path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    return HttpResponse(str(data), content_type='text/html')
