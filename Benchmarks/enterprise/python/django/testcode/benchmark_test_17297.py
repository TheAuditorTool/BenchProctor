# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest17297(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = default_blank(multipart_value)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
