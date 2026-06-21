# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest77643(request):
    host_value = request.META.get('HTTP_HOST', '')
    defusedxml.ElementTree.fromstring(str(host_value))
    return JsonResponse({"saved": True})
