# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django.http import HttpResponse


def BenchmarkTest51013(request):
    multipart_value = request.POST.get('multipart_field', '')
    checked_path = os.path.join('/var/app/data', os.path.basename(multipart_value))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
