# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest64286(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(ua_value)
    data = collected
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
