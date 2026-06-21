# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest81023(request):
    xml_value = request.body.decode('utf-8')
    data, _sep, _rest = str(xml_value).partition('\x00')
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
