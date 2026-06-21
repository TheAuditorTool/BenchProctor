# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def coalesce_blank(value):
    return value or ''

def BenchmarkTest19009(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = coalesce_blank(cookie_value)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
