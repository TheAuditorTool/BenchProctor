# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest58856(request):
    xml_value = request.body.decode('utf-8')
    data = (lambda v: v.strip())(xml_value)
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
