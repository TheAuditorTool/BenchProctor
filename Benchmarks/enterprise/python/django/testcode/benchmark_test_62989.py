# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest62989(request):
    xml_value = request.body.decode('utf-8')
    data, _sep, _rest = str(xml_value).partition('\x00')
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
