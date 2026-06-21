# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os


def BenchmarkTest78528(request):
    multipart_value = request.POST.get('multipart_field', '')
    digest = hashlib.pbkdf2_hmac('sha256', str(multipart_value).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
