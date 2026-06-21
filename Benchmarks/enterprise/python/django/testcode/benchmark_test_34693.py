# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest34693(request):
    xml_value = request.body.decode('utf-8')
    data = str(xml_value).replace('\x00', '')
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
