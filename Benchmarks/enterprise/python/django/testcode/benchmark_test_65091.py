# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os


def ensure_str(value):
    return str(value)

def BenchmarkTest65091(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = ensure_str(multipart_value)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
