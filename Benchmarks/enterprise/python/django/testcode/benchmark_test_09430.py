# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09430(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body:.200s}'
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
