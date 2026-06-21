# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest35338(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
