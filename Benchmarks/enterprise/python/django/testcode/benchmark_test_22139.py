# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest22139(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value if xml_value else 'default'
    eval(str(data))
    return JsonResponse({"saved": True})
