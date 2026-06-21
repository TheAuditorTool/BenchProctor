# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest59915(request, path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    return HttpResponse('<!-- diagnostic build token: ' + str(data) + ' -->', content_type='text/html')
