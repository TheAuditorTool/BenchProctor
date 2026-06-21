# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest69349(request):
    cookie_value = request.COOKIES.get('session_token', '')
    pending = list(str(cookie_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
