# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03603(request):
    xml_value = request.body.decode('utf-8')
    parts = str(xml_value).split(',')
    data = ','.join(parts)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
