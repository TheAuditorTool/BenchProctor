# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def coalesce_blank(value):
    return value or ''

def BenchmarkTest46921(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = coalesce_blank(ua_value)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
