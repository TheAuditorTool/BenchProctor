# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest60219(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = (lambda v: v.strip())(host_value)
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
