# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import os


def BenchmarkTest80693(request, path_param):
    path_value = path_param
    with open(os.path.join('/var/app/data', str(path_value)), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
