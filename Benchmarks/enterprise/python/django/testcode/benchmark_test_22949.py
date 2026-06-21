# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest22949(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body}'
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
