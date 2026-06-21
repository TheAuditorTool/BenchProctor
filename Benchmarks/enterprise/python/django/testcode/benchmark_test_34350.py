# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest34350(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = f'{cookie_value}'
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
