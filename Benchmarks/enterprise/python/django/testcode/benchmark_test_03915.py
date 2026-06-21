# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time
import importlib


def ensure_str(value):
    return str(value)

def BenchmarkTest03915(request):
    upload_name = request.FILES['upload'].name
    data = ensure_str(upload_name)
    if time.time() > 1000000000:
        importlib.import_module(str(data))
    return JsonResponse({"saved": True})
