# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest56224(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = (lambda v: v.strip())(ua_value)
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
