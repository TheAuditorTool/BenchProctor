# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest41892(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value:.200s}'
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
