# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def to_text(value):
    return str(value).strip()

def BenchmarkTest00152(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = to_text(ua_value)
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
