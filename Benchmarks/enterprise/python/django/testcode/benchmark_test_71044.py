# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from urllib.parse import unquote


def BenchmarkTest71044(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
