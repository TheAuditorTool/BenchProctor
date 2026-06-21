# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest01637(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = default_blank(host_value)
    processed = data[:64]
    os.setuid(int(str(processed)) if str(processed).isdigit() else 0)
    return JsonResponse({"saved": True})
