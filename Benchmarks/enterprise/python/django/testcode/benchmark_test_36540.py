# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest36540(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    defusedxml.ElementTree.fromstring(str(header_value))
    return JsonResponse({"saved": True})
