# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09408(request):
    xml_value = request.body.decode('utf-8')
    if xml_value:
        data = xml_value
    else:
        data = ''
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
