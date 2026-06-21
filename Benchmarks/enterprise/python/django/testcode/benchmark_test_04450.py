# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest04450(request):
    xml_value = request.body.decode('utf-8')
    if xml_value:
        data = xml_value
    else:
        data = ''
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
