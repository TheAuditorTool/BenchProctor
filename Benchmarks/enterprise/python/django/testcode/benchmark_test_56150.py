# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest56150(request):
    xml_value = request.body.decode('utf-8')
    data, _sep, _rest = str(xml_value).partition('\x00')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
