# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02002(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = referer_value if referer_value else 'default'
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
