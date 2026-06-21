# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def to_text(value):
    return str(value).strip()

def BenchmarkTest55586(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = to_text(forwarded_ip)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
