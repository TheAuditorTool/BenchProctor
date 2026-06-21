# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest67941(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = (lambda v: v.strip())(host_value)
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
