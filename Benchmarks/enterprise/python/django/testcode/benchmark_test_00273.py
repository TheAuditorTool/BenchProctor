# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import os


def BenchmarkTest00273(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data, _sep, _rest = str(origin_value).partition('\x00')
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
