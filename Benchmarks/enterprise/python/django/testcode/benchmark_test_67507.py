# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest67507(request):
    user_id = request.GET.get('id', '')
    digest = hashlib.sha256(('static_salt_123' + str(user_id)).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
