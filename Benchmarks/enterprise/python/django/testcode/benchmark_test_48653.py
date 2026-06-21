# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import os


def BenchmarkTest48653(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    prefix = ''
    data = prefix + str(header_value)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
