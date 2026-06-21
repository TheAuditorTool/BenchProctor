# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from urllib.parse import unquote


def BenchmarkTest81217(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = unquote(cookie_value)
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
