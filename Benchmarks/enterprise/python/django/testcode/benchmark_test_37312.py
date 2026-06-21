# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest37312(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    defusedxml.ElementTree.fromstring(str(origin_value))
    return JsonResponse({"saved": True})
