# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def BenchmarkTest62845(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data, _sep, _rest = str(origin_value).partition('\x00')
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
