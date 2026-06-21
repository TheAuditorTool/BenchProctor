# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest19153(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = '%s' % (forwarded_ip,)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
