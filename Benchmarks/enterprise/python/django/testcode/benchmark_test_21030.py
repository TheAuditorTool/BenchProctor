# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest21030(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value}'
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
