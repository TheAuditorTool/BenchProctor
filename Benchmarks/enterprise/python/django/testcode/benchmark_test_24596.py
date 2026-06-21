# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest24596(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = '%s' % str(header_value)
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
