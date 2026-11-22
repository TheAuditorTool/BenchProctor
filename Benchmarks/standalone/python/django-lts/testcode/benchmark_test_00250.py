# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.Hash import MD4


def BenchmarkTest00250(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    parts = []
    for token in str(forwarded_ip).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    digest = MD4.new(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
