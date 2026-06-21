# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest05666(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value if xml_value else 'default'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
