# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import os


def BenchmarkTest05722(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name}'
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
