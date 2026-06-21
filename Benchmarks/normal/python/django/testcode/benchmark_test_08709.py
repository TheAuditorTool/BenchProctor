# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
from django.http import HttpResponse


def BenchmarkTest08709(request, path_param):
    path_value = path_param
    data = unquote(path_value)
    return HttpResponse(str(data), content_type='text/html')
