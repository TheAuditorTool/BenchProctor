# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest42552(request):
    xml_value = request.body.decode('utf-8')
    data = '%s' % str(xml_value)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
