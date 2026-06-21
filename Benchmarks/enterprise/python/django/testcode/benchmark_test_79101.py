# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest79101(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = f'{cookie_value:.200s}'
    int(str(data))
    return JsonResponse({"saved": True})
