# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest16332(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '{}'.format(host_value)
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
