# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def relay_value(value):
    return value

def BenchmarkTest44374(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = relay_value(origin_value)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
