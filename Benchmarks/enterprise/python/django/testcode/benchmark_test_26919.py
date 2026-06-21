# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def BenchmarkTest26919(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
