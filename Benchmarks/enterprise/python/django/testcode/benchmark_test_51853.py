# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest51853(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = '{}'.format(ua_value)
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
