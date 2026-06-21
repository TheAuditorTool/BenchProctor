# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def relay_value(value):
    return value

def BenchmarkTest69310(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = relay_value(ua_value)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
