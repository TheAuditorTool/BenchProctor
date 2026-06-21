# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django.http import HttpResponse


def BenchmarkTest57316(request):
    raw_body = request.body.decode('utf-8')
    checked_path = os.path.join('/var/app/data', os.path.basename(raw_body))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
