# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest07480(request):
    xml_value = request.body.decode('utf-8')
    data = ' '.join(str(xml_value).split())
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
