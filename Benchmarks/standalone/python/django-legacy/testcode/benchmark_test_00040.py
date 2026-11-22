# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.Hash import SHA256


def BenchmarkTest00040(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    digest = SHA256.new(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
