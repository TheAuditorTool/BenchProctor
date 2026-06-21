# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09115(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = f'{forwarded_ip}'
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
