# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import os


def BenchmarkTest06085(request):
    host_value = request.META.get('HTTP_HOST', '')
    link_path = os.path.join('/var/app/data', str(host_value))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
