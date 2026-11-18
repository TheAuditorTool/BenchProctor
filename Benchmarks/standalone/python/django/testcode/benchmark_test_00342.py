# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest00342(request):
    user_id = request.GET.get('id', '')
    digest = hashlib.sha256(str(user_id).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
