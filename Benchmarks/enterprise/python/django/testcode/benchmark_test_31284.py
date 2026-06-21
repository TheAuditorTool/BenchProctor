# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest31284(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = '%s' % (ua_value,)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
