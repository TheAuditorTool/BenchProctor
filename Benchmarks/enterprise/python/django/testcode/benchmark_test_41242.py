# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest41242(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = ' '.join(str(ua_value).split())
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
