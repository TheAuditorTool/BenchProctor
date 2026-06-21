# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest64549(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = f'{cookie_value}'
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
