# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest10223(request):
    xml_value = request.body.decode('utf-8')
    if xml_value:
        data = xml_value
    else:
        data = ''
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
