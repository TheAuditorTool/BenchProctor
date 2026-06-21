# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest23639(request):
    xml_value = request.body.decode('utf-8')
    data = ' '.join(str(xml_value).split())
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
