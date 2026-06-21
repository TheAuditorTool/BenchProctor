# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def ensure_str(value):
    return str(value)

def BenchmarkTest13173(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = ensure_str(origin_value)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
