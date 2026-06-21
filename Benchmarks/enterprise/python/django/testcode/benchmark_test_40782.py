# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest40782(request):
    xml_value = request.body.decode('utf-8')
    def normalize(value):
        return value.strip()
    data = normalize(xml_value)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
