# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest74152(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '%s' % str(host_value)
    os.remove(str(data))
    return JsonResponse({"saved": True})
