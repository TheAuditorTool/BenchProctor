# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
import os


def BenchmarkTest10835(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = unquote(cookie_value)
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
