# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest01403(request):
    upload_name = request.FILES['upload'].name
    data = default_blank(upload_name)
    os.remove(str(data))
    return JsonResponse({"saved": True})
