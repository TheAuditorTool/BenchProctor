# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def coalesce_blank(value):
    return value or ''

def BenchmarkTest39931(request):
    upload_name = request.FILES['upload'].name
    data = coalesce_blank(upload_name)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
