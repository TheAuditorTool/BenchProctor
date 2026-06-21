# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os


request_state: dict[str, str] = {}

def BenchmarkTest66287(request):
    user_id = request.GET.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
