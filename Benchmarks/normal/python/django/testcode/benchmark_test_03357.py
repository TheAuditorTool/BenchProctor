# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django.http import HttpResponse


def BenchmarkTest03357(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    checked_path = os.path.join('/var/app/data', os.path.basename(referer_value))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
