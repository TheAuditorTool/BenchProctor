# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import os


def BenchmarkTest72338(request):
    upload_name = request.FILES['upload'].name
    def normalize(value):
        return value.strip()
    data = normalize(upload_name)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
