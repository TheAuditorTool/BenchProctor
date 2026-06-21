# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django.http import HttpResponse


def coalesce_blank(value):
    return value or ''

def BenchmarkTest01339(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = coalesce_blank(host_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
