# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from urllib.parse import unquote
from django.http import HttpResponse


def BenchmarkTest63582(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = unquote(referer_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
