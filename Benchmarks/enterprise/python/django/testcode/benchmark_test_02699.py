# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest02699(request):
    raw_body = request.body.decode('utf-8')
    data = default_blank(raw_body)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
