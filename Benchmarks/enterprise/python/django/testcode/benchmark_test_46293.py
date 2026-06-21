# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest46293(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data, _sep, _rest = str(forwarded_ip).partition('\x00')
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
