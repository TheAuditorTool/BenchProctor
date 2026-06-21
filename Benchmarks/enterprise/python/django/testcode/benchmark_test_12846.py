# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest12846(request):
    raw_body = request.body.decode('utf-8')
    data = str(raw_body).replace('\x00', '')
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
