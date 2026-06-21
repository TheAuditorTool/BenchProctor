# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def BenchmarkTest65877(request):
    multipart_value = request.POST.get('multipart_field', '')
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
