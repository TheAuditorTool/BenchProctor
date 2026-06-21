# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest07324(request):
    raw_body = request.body.decode('utf-8')
    data = '{}'.format(raw_body)
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
