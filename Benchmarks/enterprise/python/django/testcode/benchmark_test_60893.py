# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def BenchmarkTest60893(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    prefix = ''
    data = prefix + str(forwarded_ip)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
