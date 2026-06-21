# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
from django.http import HttpResponse


def BenchmarkTest01921(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = unquote(cookie_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
