# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest37322(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    raise RuntimeError('processing failed: ' + str(forwarded_ip))
    return JsonResponse({"saved": True})
