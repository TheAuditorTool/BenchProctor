# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest43085(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = ua_value if ua_value else 'default'
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
