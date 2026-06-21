# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import base64


def BenchmarkTest02661(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
