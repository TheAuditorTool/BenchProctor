# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest25107(request):
    cookie_value = request.COOKIES.get('session_token', '')
    with open('/var/app/data/' + str(cookie_value), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
