# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest66066(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data, _sep, _rest = str(cookie_value).partition('\x00')
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
