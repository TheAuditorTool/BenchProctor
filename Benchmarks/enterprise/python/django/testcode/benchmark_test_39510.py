# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import base64


def BenchmarkTest39510(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
