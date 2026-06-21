# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def BenchmarkTest06487(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
