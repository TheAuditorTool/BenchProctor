# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest30794(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value if xml_value else 'default'
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
