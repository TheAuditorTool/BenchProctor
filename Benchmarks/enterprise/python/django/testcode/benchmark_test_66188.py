# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def to_text(value):
    return str(value).strip()

def BenchmarkTest66188(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = to_text(auth_header)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
