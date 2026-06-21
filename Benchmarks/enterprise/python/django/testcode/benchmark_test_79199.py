# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django.http import HttpResponse


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest79199(request):
    raw_body = request.body.decode('utf-8')
    data = default_blank(raw_body)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
