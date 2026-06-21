# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os


def BenchmarkTest57305(request):
    user_id = request.GET.get('id', '')
    digest = hashlib.pbkdf2_hmac('sha256', str(user_id).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
