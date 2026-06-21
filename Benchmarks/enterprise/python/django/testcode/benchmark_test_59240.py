# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def to_text(value):
    return str(value).strip()

def BenchmarkTest59240(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = to_text(multipart_value)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
