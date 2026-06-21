# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest49516(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = str(forwarded_ip).replace('\x00', '')
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
