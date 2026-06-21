# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest01822(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = ' '.join(str(host_value).split())
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
