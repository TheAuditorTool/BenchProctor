# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest05791(request):
    xml_value = request.body.decode('utf-8')
    def normalize(value):
        return value.strip()
    data = normalize(xml_value)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
