# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import os


def BenchmarkTest67831(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    link_path = os.path.join('/var/app/data', str(header_value))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
