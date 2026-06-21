# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def relay_value(value):
    return value

def BenchmarkTest27238(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = relay_value(auth_header)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
