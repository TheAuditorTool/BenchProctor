# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def to_text(value):
    return str(value).strip()

def BenchmarkTest71348(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = to_text(host_value)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
