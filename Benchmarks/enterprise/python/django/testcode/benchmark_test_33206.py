# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest33206(request):
    xml_value = request.body.decode('utf-8')
    data = '{}'.format(xml_value)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
