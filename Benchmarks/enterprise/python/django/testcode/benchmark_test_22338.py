# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse


def BenchmarkTest22338(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
