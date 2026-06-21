# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
from django.http import HttpResponse


def BenchmarkTest43480(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    return HttpResponse('<html><body><h1>' + str(data) + '</h1></body></html>', content_type='text/html')
