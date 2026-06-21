# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest63840(request):
    xml_value = request.body.decode('utf-8')
    parts = str(xml_value).split(',')
    data = ','.join(parts)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
