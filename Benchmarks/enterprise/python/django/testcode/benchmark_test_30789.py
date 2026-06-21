# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from urllib.parse import unquote


def BenchmarkTest30789(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = unquote(cookie_value)
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
