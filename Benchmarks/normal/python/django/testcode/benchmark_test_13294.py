# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest13294(request):
    xml_value = request.body.decode('utf-8')
    data, _sep, _rest = str(xml_value).partition('\x00')
    eval(str(data))
    return JsonResponse({"saved": True})
