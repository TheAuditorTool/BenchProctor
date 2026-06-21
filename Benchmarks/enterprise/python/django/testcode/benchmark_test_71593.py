# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest71593(request):
    xml_value = request.body.decode('utf-8')
    data = str(xml_value).replace('\x00', '')
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
