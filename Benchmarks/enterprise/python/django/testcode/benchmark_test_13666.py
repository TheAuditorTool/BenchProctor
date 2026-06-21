# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os


def relay_value(value):
    return value

def BenchmarkTest13666(request):
    user_id = request.GET.get('id', '')
    data = relay_value(user_id)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
