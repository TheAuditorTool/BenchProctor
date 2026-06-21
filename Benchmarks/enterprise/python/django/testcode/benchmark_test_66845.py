# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest66845(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = '{}'.format(ua_value)
    int(str(data))
    return JsonResponse({"saved": True})
