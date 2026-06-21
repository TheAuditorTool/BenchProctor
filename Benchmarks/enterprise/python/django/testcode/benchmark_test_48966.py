# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def normalise_input(value):
    return value.strip()

def BenchmarkTest48966(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = normalise_input(ua_value)
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
