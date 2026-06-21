# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest79370(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = '%s' % str(cookie_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
