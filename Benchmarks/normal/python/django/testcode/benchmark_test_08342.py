# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def to_text(value):
    return str(value).strip()

def BenchmarkTest08342(request):
    upload_name = request.FILES['upload'].name
    data = to_text(upload_name)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
