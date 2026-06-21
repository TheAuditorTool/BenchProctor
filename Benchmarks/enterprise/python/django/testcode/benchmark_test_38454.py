# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest38454(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = '%s' % (header_value,)
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
