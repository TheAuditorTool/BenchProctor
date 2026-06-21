# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os


def normalise_input(value):
    return value.strip()

def BenchmarkTest06330(request):
    upload_name = request.FILES['upload'].name
    data = normalise_input(upload_name)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
