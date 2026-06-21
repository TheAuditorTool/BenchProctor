# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest19046(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
