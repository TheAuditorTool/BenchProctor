# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import unquote
from django.http import HttpResponse


def BenchmarkTest46656(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = unquote(cookie_value)
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
