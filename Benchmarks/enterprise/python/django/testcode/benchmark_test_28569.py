# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest28569(request):
    xml_value = request.body.decode('utf-8')
    data = '{}'.format(xml_value)
    eval(str(data))
    return JsonResponse({"saved": True})
