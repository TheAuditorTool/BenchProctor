# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest67352(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    def normalize(value):
        return value.strip()
    data = normalize(ua_value)
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
