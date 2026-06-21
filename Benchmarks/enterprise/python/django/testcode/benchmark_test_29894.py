# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import unquote
from django.http import HttpResponse


def BenchmarkTest29894(request, path_param):
    path_value = path_param
    data = unquote(path_value)
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
