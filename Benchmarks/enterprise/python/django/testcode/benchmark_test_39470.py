# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import base64


def BenchmarkTest39470(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
