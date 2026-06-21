# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest29760(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    if forwarded_ip:
        data = forwarded_ip
    else:
        data = ''
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
