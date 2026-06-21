# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest81100(request):
    host_value = request.META.get('HTTP_HOST', '')
    os.system('echo ' + str(host_value))
    return JsonResponse({"saved": True})
