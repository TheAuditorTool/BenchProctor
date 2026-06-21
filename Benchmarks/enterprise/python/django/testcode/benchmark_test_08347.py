# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def coalesce_blank(value):
    return value or ''

def BenchmarkTest08347(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = coalesce_blank(multipart_value)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
