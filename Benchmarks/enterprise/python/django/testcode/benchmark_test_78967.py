# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def coalesce_blank(value):
    return value or ''

def BenchmarkTest78967(request):
    raw_body = request.body.decode('utf-8')
    data = coalesce_blank(raw_body)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
