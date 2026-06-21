# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest64901(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = default_blank(host_value)
    os.remove(str(data))
    return JsonResponse({"saved": True})
