# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import os


def BenchmarkTest08636(request):
    host_value = request.META.get('HTTP_HOST', '')
    with open(os.path.join('/var/app/data', str(host_value)), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
