# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest70904(request):
    xml_value = request.body.decode('utf-8')
    def normalize(value):
        return value.strip()
    data = normalize(xml_value)
    eval(str(data))
    return JsonResponse({"saved": True})
