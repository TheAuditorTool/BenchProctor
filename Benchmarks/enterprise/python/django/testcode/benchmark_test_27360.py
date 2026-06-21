# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest27360(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = f'{forwarded_ip:.200s}'
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
