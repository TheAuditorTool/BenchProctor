# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest44346(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = '%s' % (cookie_value,)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
