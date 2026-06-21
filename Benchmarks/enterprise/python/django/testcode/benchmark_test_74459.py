# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest74459(request):
    xml_value = request.body.decode('utf-8')
    data, _sep, _rest = str(xml_value).partition('\x00')
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
