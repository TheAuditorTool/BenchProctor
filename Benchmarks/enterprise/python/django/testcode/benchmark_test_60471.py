# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest60471(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = '%s' % str(ua_value)
    int(str(data))
    return JsonResponse({"saved": True})
