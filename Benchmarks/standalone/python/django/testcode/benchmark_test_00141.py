# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.Hash import MD4


def BenchmarkTest00141(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body if raw_body else 'default'
    digest = MD4.new(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
