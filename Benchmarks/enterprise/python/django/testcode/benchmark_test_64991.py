# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest64991(request):
    xml_value = request.body.decode('utf-8')
    eval(str(xml_value))
    return JsonResponse({"saved": True})
