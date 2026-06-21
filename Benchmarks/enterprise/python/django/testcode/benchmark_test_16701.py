# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
from urllib.parse import unquote


def BenchmarkTest16701(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = unquote(multipart_value)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
