# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def BenchmarkTest05319(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value:.200s}'
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
