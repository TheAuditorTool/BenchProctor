# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def BenchmarkTest43431(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
