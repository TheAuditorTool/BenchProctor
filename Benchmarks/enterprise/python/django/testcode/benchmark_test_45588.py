# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest45588(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data, _sep, _rest = str(origin_value).partition('\x00')
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
