# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django.http import HttpResponse


def relay_value(value):
    return value

def BenchmarkTest74362(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = relay_value(header_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
