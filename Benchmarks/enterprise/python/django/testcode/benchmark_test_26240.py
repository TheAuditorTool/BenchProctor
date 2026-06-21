# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest26240(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    prefix = ''
    data = prefix + str(origin_value)
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
