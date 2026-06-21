# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest06501(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    parts = []
    for token in str(header_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
