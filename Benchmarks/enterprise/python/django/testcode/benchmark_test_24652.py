# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest24652(request):
    host_value = request.META.get('HTTP_HOST', '')
    os.remove(str(host_value))
    return JsonResponse({"saved": True})
