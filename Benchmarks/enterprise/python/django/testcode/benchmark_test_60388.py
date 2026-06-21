# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest60388(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body if raw_body else 'default'
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
