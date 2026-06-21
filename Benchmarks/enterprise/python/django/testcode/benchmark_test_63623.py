# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest63623(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = origin_value if origin_value else 'default'
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
