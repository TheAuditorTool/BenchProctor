# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest55884(request):
    xml_value = request.body.decode('utf-8')
    data = '{}'.format(xml_value)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
