# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01527(request):
    xml_value = request.body.decode('utf-8')
    if xml_value:
        data = xml_value
    else:
        data = ''
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
