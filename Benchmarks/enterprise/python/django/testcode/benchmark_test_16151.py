# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest16151(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '%s' % str(origin_value)
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
