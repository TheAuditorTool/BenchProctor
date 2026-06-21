# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse


def BenchmarkTest54619(request, path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
