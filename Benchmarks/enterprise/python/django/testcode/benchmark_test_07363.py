# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse


def BenchmarkTest07363(request, path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
