# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def coalesce_blank(value):
    return value or ''

def BenchmarkTest38395(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = coalesce_blank(referer_value)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
