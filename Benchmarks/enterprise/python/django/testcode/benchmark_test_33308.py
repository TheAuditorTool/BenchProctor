# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest33308(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value}'
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
