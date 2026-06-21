# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django.http import HttpResponse


def to_text(value):
    return str(value).strip()

def BenchmarkTest06986(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = to_text(referer_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
