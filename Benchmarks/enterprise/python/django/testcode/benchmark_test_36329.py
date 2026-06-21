# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest36329(request):
    xml_value = request.body.decode('utf-8')
    def normalize(value):
        return value.strip()
    data = normalize(xml_value)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
