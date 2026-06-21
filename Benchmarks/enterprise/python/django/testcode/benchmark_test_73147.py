# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest73147(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = (lambda v: v.strip())(forwarded_ip)
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
