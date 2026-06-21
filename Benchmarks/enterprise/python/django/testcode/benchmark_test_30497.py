# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest30497(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = '%s' % (cookie_value,)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
