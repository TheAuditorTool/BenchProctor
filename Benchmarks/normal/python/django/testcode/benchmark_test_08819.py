# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest08819(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = host_value if host_value else 'default'
    os.remove(str(data))
    return JsonResponse({"saved": True})
