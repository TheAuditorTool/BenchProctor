# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03780(request):
    xml_value = request.body.decode('utf-8')
    data = (lambda v: v.strip())(xml_value)
    eval(str(data))
    return JsonResponse({"saved": True})
