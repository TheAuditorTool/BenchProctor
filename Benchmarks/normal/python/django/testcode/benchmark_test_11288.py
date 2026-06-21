# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
from urllib.parse import unquote


def BenchmarkTest11288(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = unquote(referer_value)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
