# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest50266(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
