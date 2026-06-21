# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest80995(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = '%s' % (ua_value,)
    eval(str(data))
    return JsonResponse({"saved": True})
