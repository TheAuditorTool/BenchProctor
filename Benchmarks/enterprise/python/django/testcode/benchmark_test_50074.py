# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest50074(request):
    xml_value = request.body.decode('utf-8')
    if xml_value:
        data = xml_value
    else:
        data = ''
    int(str(data))
    return JsonResponse({"saved": True})
