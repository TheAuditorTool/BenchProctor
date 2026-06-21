# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def to_text(value):
    return str(value).strip()

def BenchmarkTest33212(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = to_text(origin_value)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
