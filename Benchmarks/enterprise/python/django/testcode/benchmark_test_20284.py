# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest20284(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    parts = []
    for token in str(header_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
