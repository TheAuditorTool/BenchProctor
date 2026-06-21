# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os


def BenchmarkTest26727(request):
    upload_name = request.FILES['upload'].name
    digest = hashlib.pbkdf2_hmac('sha256', str(upload_name).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
