# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django.http import HttpResponse


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest36263(request):
    xml_value = request.body.decode('utf-8')
    data = default_blank(xml_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
