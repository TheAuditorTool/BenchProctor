# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django.http import HttpResponse


def BenchmarkTest19648(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    checked_path = os.path.join('/var/app/data', os.path.basename(header_value))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
