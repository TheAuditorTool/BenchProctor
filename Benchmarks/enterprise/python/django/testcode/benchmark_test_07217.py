# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest07217(request):
    xml_value = request.body.decode('utf-8')
    data = '%s' % str(xml_value)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
