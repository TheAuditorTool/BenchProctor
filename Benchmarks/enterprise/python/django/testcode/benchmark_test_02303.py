# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02303(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = '%s' % (cookie_value,)
    eval(str(data))
    return JsonResponse({"saved": True})
