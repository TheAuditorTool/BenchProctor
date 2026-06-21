# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest73706(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    defusedxml.ElementTree.fromstring(str(auth_header))
    return JsonResponse({"saved": True})
