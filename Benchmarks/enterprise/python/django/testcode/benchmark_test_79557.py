# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest79557(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value if xml_value else 'default'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
