# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest34914(request, path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    return HttpResponse('<html><body><h1>' + str(data) + '</h1></body></html>', content_type='text/html')
