# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest21377(request):
    xml_value = request.body.decode('utf-8')
    data = '%s' % str(xml_value)
    eval(str(data))
    return JsonResponse({"saved": True})
