# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32770(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body if raw_body else 'default'
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
