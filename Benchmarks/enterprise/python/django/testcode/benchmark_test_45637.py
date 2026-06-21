# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest45637(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '%s' % str(origin_value)
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
