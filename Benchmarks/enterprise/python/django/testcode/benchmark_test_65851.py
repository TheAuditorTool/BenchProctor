# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest65851(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data, _sep, _rest = str(header_value).partition('\x00')
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
