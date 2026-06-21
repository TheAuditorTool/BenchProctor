# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest28903(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = host_value if host_value else 'default'
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
