# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.Hash import SHA256


def BenchmarkTest00104(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = '{}'.format(forwarded_ip)
    digest = SHA256.new(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
