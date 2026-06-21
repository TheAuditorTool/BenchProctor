# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest73709(request):
    xml_value = request.body.decode('utf-8')
    prefix = ''
    data = prefix + str(xml_value)
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
