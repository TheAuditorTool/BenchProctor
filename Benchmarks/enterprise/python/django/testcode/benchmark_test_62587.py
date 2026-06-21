# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest62587(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value if xml_value else 'default'
    int(str(data))
    return JsonResponse({"saved": True})
