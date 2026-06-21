# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest29429(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = '%s' % str(ua_value)
    exec(str(data))
    return JsonResponse({"saved": True})
