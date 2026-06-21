# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00826(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = f'{cookie_value:.200s}'
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
