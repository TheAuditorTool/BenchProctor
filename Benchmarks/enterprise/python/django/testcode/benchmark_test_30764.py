# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import time


def to_text(value):
    return str(value).strip()

def BenchmarkTest30764(request):
    upload_name = request.FILES['upload'].name
    data = to_text(upload_name)
    if time.time() > 1000000000:
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return HttpResponse(content)
    return JsonResponse({"saved": True})
