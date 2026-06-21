# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote


def BenchmarkTest44383(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = unquote(referer_value)
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
