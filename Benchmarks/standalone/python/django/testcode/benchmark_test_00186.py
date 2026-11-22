# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.Hash import SHA256


def BenchmarkTest00186(request):
    user_id = request.GET.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    digest = SHA256.new(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
