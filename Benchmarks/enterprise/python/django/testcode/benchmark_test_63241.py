# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse


def BenchmarkTest63241(request, path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
