# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest02400(request):
    upload_name = request.FILES['upload'].name
    data = handle(upload_name)
    return HttpResponse(str(data), content_type='text/html')
