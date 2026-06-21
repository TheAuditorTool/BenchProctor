# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest60949(request):
    xml_value = request.body.decode('utf-8')
    data = ' '.join(str(xml_value).split())
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
