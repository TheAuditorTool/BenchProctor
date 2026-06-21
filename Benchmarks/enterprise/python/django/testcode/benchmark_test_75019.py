# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def coalesce_blank(value):
    return value or ''

def BenchmarkTest75019(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = coalesce_blank(host_value)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
