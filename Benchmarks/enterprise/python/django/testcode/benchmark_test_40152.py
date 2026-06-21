# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django.http import HttpResponse


def normalise_input(value):
    return value.strip()

def BenchmarkTest40152(request):
    upload_name = request.FILES['upload'].name
    data = normalise_input(upload_name)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
