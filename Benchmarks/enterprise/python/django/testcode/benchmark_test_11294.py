# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import os


def BenchmarkTest11294(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    link_path = os.path.join('/var/app/data', str(origin_value))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
