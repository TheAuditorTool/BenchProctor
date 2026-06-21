# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest10596(request):
    user_id = request.GET.get('id', '')
    digest = str(user_id).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
