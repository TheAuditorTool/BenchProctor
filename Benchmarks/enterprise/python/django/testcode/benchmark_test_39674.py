# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest39674(request):
    xml_value = request.body.decode('utf-8')
    with open('output.csv', 'a') as fh:
        fh.write(str(xml_value) + ',data\n')
    return JsonResponse({"saved": True})
