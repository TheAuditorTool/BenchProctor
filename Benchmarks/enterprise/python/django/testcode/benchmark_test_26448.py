# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest26448(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = '%s' % (cookie_value,)
    if str(data) == 'fluffy':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
