# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest00106(request):
    cookie_value = request.COOKIES.get('session_token', '')
    kind = 'json' if str(cookie_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(cookie_value).strip()
        case _:
            data = str(cookie_value)
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
