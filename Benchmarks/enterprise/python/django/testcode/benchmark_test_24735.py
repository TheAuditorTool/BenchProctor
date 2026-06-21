# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest24735(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    digest = hashlib.sha256(str(header_value).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
