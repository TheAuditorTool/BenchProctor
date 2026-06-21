# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest54707(request):
    raw_body = request.body.decode('utf-8')
    defusedxml.ElementTree.fromstring(str(raw_body))
    return JsonResponse({"saved": True})
