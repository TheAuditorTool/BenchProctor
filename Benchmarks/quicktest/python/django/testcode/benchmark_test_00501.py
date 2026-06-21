# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00501(request):
    raw_body = request.body.decode('utf-8')
    data = (lambda v: v.strip())(raw_body)
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
