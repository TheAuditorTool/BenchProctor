# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest65722(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value}'
    os.seteuid(65534)
    return JsonResponse({"saved": True})
