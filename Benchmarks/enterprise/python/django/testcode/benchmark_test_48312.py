# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def normalise_input(value):
    return value.strip()

def BenchmarkTest48312(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = normalise_input(referer_value)
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
