# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from urllib.parse import unquote


def BenchmarkTest77454(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = unquote(referer_value)
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
