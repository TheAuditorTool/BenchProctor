# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest80834(request):
    xml_value = request.body.decode('utf-8')
    parts = str(xml_value).split(',')
    data = ','.join(parts)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
