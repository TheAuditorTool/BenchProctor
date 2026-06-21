# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest56425(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value if xml_value else 'default'
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
