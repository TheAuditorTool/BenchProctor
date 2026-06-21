# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest05663(request):
    cookie_value = request.COOKIES.get('session_token', '')
    return HttpResponse(str(cookie_value), content_type='text/html')
