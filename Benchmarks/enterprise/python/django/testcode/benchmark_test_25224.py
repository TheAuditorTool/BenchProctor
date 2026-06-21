# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest25224(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '%s' % (host_value,)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
