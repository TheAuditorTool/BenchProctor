# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest66202(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = '%s' % (cookie_value,)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
