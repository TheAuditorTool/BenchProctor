# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from urllib.parse import unquote


def BenchmarkTest49343(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = unquote(referer_value)
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
